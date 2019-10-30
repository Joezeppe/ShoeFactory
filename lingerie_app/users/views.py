from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render, redirect


# Create your views here.
from .forms import UserForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now log in')
            return redirect('users:login')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})