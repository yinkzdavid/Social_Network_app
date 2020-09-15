from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts" 
urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.view_profile, name="view_profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('change-password/', views.change_password, name="change_password"),
    # path('reset-password/', password_reset, name='reset_password'),
    # path('reset-password/done', password_reset_done, name='password_reset_done'),

]
