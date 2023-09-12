from django.contrib import admin
from .models import Contact

# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_user', 'alias', 'date_added', 'is_friend')
    readonly_fields = ('date_added',)
    ordering=('-date_added',)

admin.site.register(Contact, contactAdmin)