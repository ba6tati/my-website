from django.urls import path

from .views import AppsView, app_view, post_comment

app_name = 'apps'
urlpatterns = [
    path('', AppsView.as_view(), name='apps'),
    path('<int:pk>/', app_view, name='app'),
    path('post_comment/', post_comment, name='post_comment'),
]