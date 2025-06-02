from django.urls import path
from . import api

urlpatterns = [
    path('register/', api.RegisterView.as_view(), name='register'),
    path('login/', api.login_view, name='login'),
    path('logout/', api.logout_view, name='logout'),
    path('profile/', api.ProfileView.as_view(), name='profile'),
]
