from django.contrib import admin
from django.urls import path
from django.conf import settings
from apps.users.views import admin_list,  register_admin

urlpatterns = [
    path('', admin_list, name='admin_list'),
    path('register/', register_admin, name='register_admin'),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
