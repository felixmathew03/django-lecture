from django import forms
from .views import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' # ["username","password"]