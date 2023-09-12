from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
from .forms import RegistrationForm
from .models import Account, UserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from transfer.models import Transfer

# Create your views here.

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            username=email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.phone_number = phone_number
            user.save()

            userprofile = UserProfile()
            userprofile.user_id = user.id
            userprofile.profile_picture = 'default/default-user.png'
            userprofile.save()

            current_site=get_current_site(request)
            mail_subject="Activa tu cuenta de Inter Banco"
            body=render_to_string('accounts/account_verification_email.html',{
                "user":user,
                "domain":current_site,
                "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                "token":default_token_generator.make_token(user)
            })
            to_email=email
            send_email=EmailMessage(mail_subject, body, to=[to_email])
            send_email.send()

            return redirect('/accounts/login/?command=verification&email='+email)

    context = {
        'form':form
    }

    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Haz iniciado sesion exitosamente")
            
            url=request.META.get('HTTP_REFERER')

            try:
                query = requests.utils.urlparse(url).query
                params=dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                #incluir redirect a wallet
                return redirect('bank')

            return redirect('bank')
        else:
            messages.error(request, 'Las credenciales son incorrectas')
        
    return render(request, 'accounts/login.html')
    
@login_required(login_url='login')
def log_out(request):
    logout(request)
    messages.success(request, "Haz salido de sesion")
    return redirect('bank')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Felicidades tu cuenta esta activa!")
        return redirect('login')
    else:
        messages.error(request, "Lo siento la activacion ha sido invalida!")
        return redirect('register')

@login_required(login_url='login')
def wallet(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    context = {
        "userprofile":userprofile
    }
    return render(request, "accounts/wallet.html", context)

def my_transfer(request):
    transfers = Transfer.objects.filter(user_id=request.user.id).order_by('-date_added')
    transfers_count = transfers.count()
    context = {
        "transfers":transfers,
        "transfers_count": transfers_count
    }
    return render(request, "accounts/my_transfers.html", context)
