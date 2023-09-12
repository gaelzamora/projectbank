from django.db import models
from accounts.models import Account, UserProfile

# Create your models here.

class Contact(models.Model):
    user=models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user")
    contact_user=models.ForeignKey(Account, on_delete=models.CASCADE, related_name="contact_user", null=True)
    alias = models.CharField(max_length=20)
    date_added=models.DateTimeField(auto_now_add=True)
    is_friend=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.full_name} Contact: {self.profile_contact.user.full_name}'