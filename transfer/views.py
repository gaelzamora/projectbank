from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Account, UserProfile
from django.contrib import messages
from .models import Transfer
import datetime
from django.db.models import Q
# Create your views here.

@login_required(login_url='login')
def transfer(request):
    amount=None
    if request.method=='POST':
        email = request.POST['email']
        #try:
        amount = int(request.POST['amount'])
        password = request.POST['password']
        user = Account.objects.get(username__exact=request.user.username)

        success = user.check_password(password)
            #try:
        if success:
                    user_destiny = Account.objects.get(email__exact=email)
                    if user_destiny:
                        if user_destiny!=user:
                            if amount == "":
                                messages.warning(request, "Debes ingresar un monto!")
                            if amount <= user.amount:
                                    user.amount -= amount
                                    user_destiny.amount += amount
                                    user.save()
                                    user_destiny.save()
                                    messages.success(request, "La transaccion ha sido exitosa")
                                    yr=int(datetime.date.today().strftime('%Y'))
                                    mt=int(datetime.date.today().strftime('%m'))
                                    dt=int(datetime.date.today().strftime('%d'))
                                    d=datetime.date(yr,mt,dt)

                                    current_date=d.strftime('%Y%m%d')
                                    transfer_id=current_date + str(user.id)

                                    transfer = Transfer.objects.create(
                                         user_id=request.user.id,
                                         amount=amount, 
                                         email_destiny=user_destiny.email, 
                                         transfer_id=transfer_id)
                                    transfer.save()
                                    #messages.error(request, "Algo ha salido mal, reportate con soporte para solucionarlo")
                                    #return redirect('transfer')
                            else:
                                messages.error(request, "No tienes el suficiente monto para hacer la transaccion")
                        else:
                            messages.error(request, "No puedes mandar transferencias a tu misma cuenta")
                    else:
                        messages.error(request, "No se encontro ninguna cuenta con ese email")

        else:
                messages.error(request, "No se pudo realizar la transaccion, la contraseña es invalida")
                return redirect('transfer')
            #except:
                #messages.error(request, "Algo ha salido mal")
        #except:
            #messages.error(request, "Algo salio mal")
    return render(request, "transfer/transfer.html")

def search_account(request):
    user=None
    username=None
    keyword=None
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword == "":
            return redirect('transfer')
        user=Account.objects.get(Q(phone_number__icontains=keyword) | Q(email__icontains=keyword) | Q(username__icontains=keyword))
        username=UserProfile.objects.get(username_id=user.id)
    context = {
         "user":user,
         "username":username,
         "keyword":keyword
    }
    return render(request, "transfer/preview.html", context)
                                   