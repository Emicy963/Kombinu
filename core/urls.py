from django.contrib import admin
from django.urls import path, include
from accounts.views import start_view
from dasboard.views import home_view, dashboard_overview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('dashboard/', dashboard_overview, name='overview'),
    path('login/', start_view, name='login'),
    #path('accounts/', include('accounts.urls')),
    #path('dashboard/', home_view, name='dashboard'),
]
