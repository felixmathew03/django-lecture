from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,label='USERNAME',widget=forms.TextInput(attrs={"placeholder":"Enter username"}))
    password = forms.CharField(label='PASSWORD',widget=forms.PasswordInput(attrs={"placeholder":"Enter password"}))