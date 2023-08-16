from django.db import models
from accounts.models import Account


# Create your models here.

class Transfer(models.Model):
    transfer_id=models.CharField(max_length=50)
    date_added=models.DateField(auto_now_add=True)
    amount=models.CharField(max_length=40)
    destiny_account=models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.transfer_id

    