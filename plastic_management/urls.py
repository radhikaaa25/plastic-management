from django.urls import path
from . import views

urlpatterns = [
    # Page URLs
    path('', views.login_page, name='login_page'), 
    path('home/', views.home_page, name='home_page'),
    path('qr-scanner/', views.qr_scanner_page, name='qr_scanner_page'),

    # API URLs
    path('api/login/', views.login_register_api, name='login_api'),
    path('api/deposit/', views.deposit_api, name='deposit_api'),
    path('api/balance/', views.balance_api, name='balance_api'),
    path('api/qr-scan/', views.qr_scan_api, name='qr_scan_api'),
    path('api/stats/', views.stats_api, name='stats_api'),
    path('api/generate-qr/', views.generate_qr_codes, name='generate_qr_codes'),
]