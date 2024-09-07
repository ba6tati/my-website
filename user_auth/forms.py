from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import EmailField

from .models import User

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    email = EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']