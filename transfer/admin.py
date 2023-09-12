from django.contrib import admin
from .models import Transfer

# Register your models here.
class transferAdmin(admin.ModelAdmin):
    list_display = ['transfer_id', 'date_added', 'user', 'amount', 'email_destiny']

admin.site.register(Transfer, transferAdmin)