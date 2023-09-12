from django.db import models
from accounts.models import Account


# Create your models here.

class Transfer(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    transfer_id=models.CharField(max_length=12)
    amount=models.CharField(max_length=20)
    email_destiny=models.CharField(max_length=30)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.transfer_id

    