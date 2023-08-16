from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def transfer(request):
    if request.method=='POST':
        email = request.GET['email']
        amount = request.POST['amount']
        password = request.POST['password']

        user = Account.objects.get(username__exact=request.user.username)

        success = user.check_password(password)

        if success:
            user_destiny = Account.objects.get(email__exact=email)
            if user_destiny:
                if amount <= user.amount:
                    try:
                        user.amount -= amount
                        user_destiny.amount += amount
                        user.save()
                        user_destiny.save()
                        messages.success(request, "La transaccion ha sido exitosa")
                    except:
                        messages.error(request, "Algo ha salido mal, reportate con soporte para solucionarlo")
                        return redirect('transfer')
                else:
                    messages.error(request, "No tienes el suficiente monto para hacer la transaccion")
            else:
                messages.error(request, "La cuenta de email que ingresaste no existe")

        else:
            messages.error(request, "No se pudo realizar la transaccion, la contraseña es invalida")
            return redirect('transfer')
    return render(request, "transfer/transfer.html")