from django.urls import path

from .views import AppsView, app_view

app_name = 'apps'
urlpatterns = [
    path('', AppsView.as_view(), name='apps'),
    path('<int:pk>/', app_view, name='app'),
]