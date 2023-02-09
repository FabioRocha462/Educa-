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
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "image",
        ]
        def __init__(self, *args, **kwargs):
            super(UpdateForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

class UpdateTypeUser(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "typeUser",
        ]
        
        def __init__(self, *args, **kwargs):
            super(UpdateTypeUser, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'