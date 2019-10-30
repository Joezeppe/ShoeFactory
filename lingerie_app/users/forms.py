from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create the form class.


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': 'Please enter your real email. This is where you will get your confirmations and invoices',
            'password1': None,
            'password2': None
        }

