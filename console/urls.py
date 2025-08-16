from django.urls import path
from django.contrib.auth import views as auth_views # view de login/logout built-in do Django

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='console/login.html'), name='login'), # Login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # Logout
]