from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view, register_view
from dasboard.views import home_view, dashboard_overview, termos_condicoes
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('dashboard/', dashboard_overview, name='overview'),
    path('temos_condicoes/', termos_condicoes, name='termos'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    #path('accounts/', include('accounts.urls')),
    #path('dashboard/', home_view, name='dashboard'),

    # API urls
    path('api/auth/', include('accounts.urls_api')),
    path('api/courses/', include('courses.urls')),

    # Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
