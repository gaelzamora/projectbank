from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
from .forms import RegistrationForm
from .models import Account

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
            user = Account.objects.create_user(first_name, last_name, username, email, password)
            user.phone_number = phone_number
            user.save()

            
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