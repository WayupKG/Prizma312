from django.urls import path

from .views import *


urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register')
]
