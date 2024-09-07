from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.views.generic import TemplateView, DetailView

from .forms import RegisterForm
from .models import User

class UserLoginView(LoginView):
    template_name = 'user_auth/login.html'

def logout_view(request):
    logout(request)
    return redirect('auth:login')

"""


class UserProfileView(DetailView):
    model = models.User
    template_name = 'user_auth/profile.html'
"""

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            if user:
                login(request, user)
                return redirect('home')  # Redirect to a success page or home
            else:
                # Handle case where user is not returned
                print("User object is None")
                
            return redirect('home')
    else:
        form = RegisterForm()
            
    return render(request, 'user_auth/register.html', {'form': form})
