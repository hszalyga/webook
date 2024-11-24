from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'password1': '<PASSWORD>',
            'password2': '<PASSWORD confirmation>',
        }
        error_messages = {
            'password_mismatch': 'The two password fields didn\'t match.'
        }