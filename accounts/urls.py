from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    path('me/', views.index, name='my_account'),
    path('<str:username>/', views.AccountView.as_view(), name='account'),
]