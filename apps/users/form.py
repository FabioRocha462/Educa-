from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()
class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =[
            "username",
            "email",
            "image",
            "typeUser",
            "password1",
            "password2"
        ]

class UpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "image",
        ]

class UpdateTypeUser(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "typeUser",
        ]