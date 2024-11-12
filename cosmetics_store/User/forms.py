from django import forms
from phonenumber_field.formfields import PhoneNumberField


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Register(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = PhoneNumberField(region='RU')
    age = forms.IntegerField(max_value=120)