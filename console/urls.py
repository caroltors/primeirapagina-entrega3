from django.urls import path
from django.contrib.auth import views as auth_views # view de login/logout built-in do Django
from . import views # Importa as views do app console

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='console/login.html'), name='login'), # Login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # Logout
    path('certificates/', views.certificate_list, name='certificate_list'), # Lista de certificados
    path('certificates/create/', views.certificate_create, name='certificate_create'), # Criação de certificado
    path('certificates/edit/<int:pk>/', views.certificate_update, name='certificate_edit'), # Edição de certificado
    path('certificates/delete/<int:pk>/', views.certificate_delete, name='certificate_delete'), # Exclusão de certificado
    path('vendorvpn/', views.vendorvpn_list, name='vendorvpn_list'), # Lista de VPNs de fornecedores
    path('vendorvpn/create/', views.vendorvpn_create, name='vendorvpn_create'), # Criação de VPN de fornecedor
    path('vendorvpn/edit/<int:pk>/', views.vendorvpn_update, name='vendorvpn_edit'), # Edição de VPN de fornecedor
    path('vendorvpn/delete/<int:pk>/', views.vendorvpn_delete, name='vendorvpn_delete'), # Exclusão de VPN de fornecedor
    path('applications/', views.application_list, name='application_list'), # Lista de aplicações
    path('applications/create/', views.application_create, name='application_create'), # Criação de aplicação
    path('applications/edit/<int:pk>/', views.application_update, name='application_edit'), # Edição de aplicação
    path('applications/delete/<int:pk>/', views.application_delete, name='application_delete'), # Exclusão de aplicação
    path('dashboard/', views.dashboard, name='dashboard'), # Dashboard principal
]
