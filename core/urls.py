from django.contrib import admin
from django.urls import path, include
from accounts.views import start_view
from dasboard.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_view, name='home'),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', home_view, name='dashboard'),
]
