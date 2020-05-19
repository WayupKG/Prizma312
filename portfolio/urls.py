from django.urls import path

from .views import *

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('add/', CreatePortfolioView.as_view(), name='create_portfolio')
]
