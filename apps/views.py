from django.shortcuts import render
from django.views.generic import ListView

from .models import App

class AppsView(ListView):
    template_name = "apps/index.html"
    context_object_name = "latest_apps"

    def get_queryset(self):
        return App.objects.order_by('release_date')[:20]
    
def app_view(request, pk):
    app = App.objects.get(pk=pk)
    return render(request, 'apps/app.html', {'app': app})