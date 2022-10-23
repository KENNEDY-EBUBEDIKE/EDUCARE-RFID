from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class StudentProfileManager(models.Manager):

    def create_student(self, first_name, surname, classs):
        if not first_name:
            raise ValueError('First Name IS REQUIRED!!')
        if not surname:
            raise ValueError('Surname IS REQUIRED!!')
        student = self.model(first_name=first_name, surname=surname, classs=classs)
        student.save(using=self._db)
        return student


class Student(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    classs = models.CharField(max_length=255, null=True, blank=True)

    photo = models.ImageField(upload_to='image/')

    rfid_code = GenericRelation('CodeBase', related_query_name='student_profile')

    objects = StudentProfileManager()

    class Meta:
        ordering = ('surname',)

    def __str__(self):
        return f'{self.surname} {self.first_name}'

    def get_rfid_code(self):
        code = self.rfid_code.all()
        if code:
            return code[0].rfid_code
        else:
            return None


class CodeBase(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    owner = GenericForeignKey("content_type", "object_id")
    rfid_code = models.CharField(unique=True, blank=True, null=True, max_length=20)
    last_scan = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        return f'{self.owner.surname} {self.owner.first_name} => {self.rfid_code}'
