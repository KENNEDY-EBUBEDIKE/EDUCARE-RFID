from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import update_rfid_code, scan_student

urlpatterns = [
    path('update-rfid-code/', update_rfid_code, name='update_rfid_code'),
    path('scan-student/', scan_student, name='scan_student'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
