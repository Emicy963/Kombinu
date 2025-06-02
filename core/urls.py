from django.contrib import admin
from django.urls import path, include
from accounts.views import start_view
from dasboard.views import home_view, dashboard_overview, termos_condicoes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('dashboard/', dashboard_overview, name='overview'),
    path('temos_condicoes/', termos_condicoes, name='termos'),
    path('login/', start_view, name='login'),
    #path('accounts/', include('accounts.urls')),
    #path('dashboard/', home_view, name='dashboard'),

    # API urls
    path('api/', include('accounts.urls_api')),
]
