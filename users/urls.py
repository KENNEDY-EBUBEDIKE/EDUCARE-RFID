from django.conf import settings
from django.urls import path
from .views import register, users, update_rfid_code, scan_profile


urlpatterns = [
    path('', users, name='users'),
    path('register/', register, name='register'),
    path('users/', users, name='users'),
    path('update-rfid-code/<int:user_id>/', update_rfid_code, name='update_rfid_code'),
    path('scan-profile/', scan_profile, name='scan_profile'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
