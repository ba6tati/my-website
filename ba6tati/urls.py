from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls', namespace='auth')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('apps/', include('apps.urls', namespace='apps')),
]