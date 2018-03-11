from django.urls import path, re_path
from . import views
from django.contrib.auth.views import (
login, logout, password_reset, password_reset_done, password_reset_confirm,
password_reset_complete
)

urlpatterns = [
    path('', views.home),
    path('login/', login, {'template_name':'accounts/login.html'}),
    path('logout/', logout, {'template_name':'accounts/logout.html'}),
    path('register/', views.register, name = 'register'),
    path('profile/', views.view_profile, name = 'view_profile'),
    path('profile/edit/', views.edit_profile, name = 'edit_profile'),
    path('profile/change_password/', views.change_password, name = 'change_password'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    re_path(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset/complete/', password_reset_complete, name='password_reset_complete')
]
