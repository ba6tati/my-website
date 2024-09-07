from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

from user_auth.models import User

@login_required
def index(request):
    user = request.user
    return render(request, 'account/index.html', {'user': user})

class AccountView(DetailView):
    model = User
    template_name = "account/account.html"
    
    def get_object(self, queryset=None):
        # Get the username from the URL
        username = self.kwargs.get('username')
        # Retrieve the user object based on the username
        return get_object_or_404(User, username=username)