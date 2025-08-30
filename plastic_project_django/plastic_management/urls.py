from django.urls import path
from . import views

urlpatterns = [
    # Page URLs
    path('', views.login_page, name='login_page'), 
    path('home/', views.home_page, name='home_page'),

    # API URLs
    path('api/login/', views.login_register_api, name='login_api'),
    path('api/deposit/', views.deposit_api, name='deposit_api'),
    path('api/balance/', views.balance_api, name='balance_api'),
]