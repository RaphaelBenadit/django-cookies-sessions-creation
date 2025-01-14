# myapp/forms.py
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    email = forms.EmailField(label='Email')
