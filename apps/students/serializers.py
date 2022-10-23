from rest_framework import serializers
from .models import Student


class StudentProfileSerializer(serializers.ModelSerializer):
    rfid_code = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = "__all__"

    def get_rfid_code(self, obj):
        return obj.get_rfid_code()
