from django.contrib import admin
from django.urls import path, include, register_converter
from django.conf import settings
from django.conf.urls.static import static
from crops import views as crop_views
from .converters import RegionConverter

# Register the custom URL converter
register_converter(RegionConverter, 'region')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),
    path('login/', include('users.urls')),
    path('dashboard/', crop_views.dashboard, name='dashboard'),
    path('dashboard/<region:region>/', crop_views.dashboard_by_region, name='dashboard_by_region'),
    path('crops/<region:region>/', crop_views.crops_by_region, name='crops_by_region'),
    path('', crop_views.home, name='home'),  # Home page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)