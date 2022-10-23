from django.contrib import admin
from django.urls import path
from django.conf import settings
from apps.students.pages.views import students_list, add_student, scan_student_page


urlpatterns = [

    path('', students_list, name='students_list'),
    path('add-student/', add_student, name='add_student'),
    path('add-student/', add_student, name='add_student'),
    path('scan-student/', scan_student_page, name='scan_student_page'),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
