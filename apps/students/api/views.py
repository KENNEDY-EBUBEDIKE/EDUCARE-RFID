from rest_framework.response import Response
from rest_framework.decorators import api_view
from utils import rfid_code_utilities
from apps.students.serializers import StudentProfileSerializer
from apps.students.models import Student
from rest_framework import status


@api_view(["POST"])
def scan_student(request):
    owner = rfid_code_utilities.check_owner(request.data['code'])

    if owner:
        ser_student = StudentProfileSerializer(owner)
        return Response(
            data={
                "success": True,
                "student": ser_student.data,
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            data={
                "success": False,
            },
            status=status.HTTP_200_OK
        )


@api_view(['PATCH'])
def update_rfid_code(request):
    if request.method == "PATCH":
        student = Student.objects.get(id=request.data['pk'])
        resp = rfid_code_utilities.update_rfid_code(student, request.data['rfid_code'])
        ser_student = StudentProfileSerializer(student)
        if resp["success"]:
            return Response(
                data={
                    "success": True,
                    "message": "Updated Successfully",
                    "student": ser_student.data,
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    "success": False,
                    "message": f'This RFID Card belongs to {resp["owner"].surname} {resp["owner"].first_name}'
                },
                status=status.HTTP_200_OK
            )
