from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingresa Contraseña',
        'class': 'form-control',
        'id': 'password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar Contraseña',
        'class': 'form-control',
        'id': 'confirmPassword'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Ingresa Nombre'
        self.fields['last_name'].widget.attrs['placeholder']='Ingresa Apellido'
        self.fields['phone_number'].widget.attrs['placeholder']='Ingresa Numero Telefonico'
        self.fields['email'].widget.attrs['placeholder']='Ingresa Email'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
    def clean(self):
        cleaned_data=super(RegistrationForm, self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'El password no coincide!'
            )