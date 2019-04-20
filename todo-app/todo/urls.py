from django.contrib import admin
from django.urls import path, include
import accounts
import App

urlpatterns = [
    path('App/', include('App.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
