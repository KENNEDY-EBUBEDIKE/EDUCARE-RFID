import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from .models import User
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
import re


def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        appointment = request.POST.get('appointment')
        photo = request.FILES.get('photo')

        try:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.is_staff = True
            if photo:
                new_user.photo = photo
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.address = address
            new_user.phone_number = phone_number
            new_user.appointment = appointment
            new_user.save()
        except IntegrityError as e:
            return render(request, 'register.html', {'msg': e})
        return redirect(resolve_url(users))

    return render(request, 'register.html')


def users(request):
    all_users = User.objects.all()
    return render(request, 'users.html', {'users': all_users})


def update_rfid_code(request, user_id):
    if request.method == "POST":
        code = request.POST.get('code').strip()
        code = re.sub(r'[\x00-\x1F]+', '', code)
        user = User.objects.get(pk=user_id)
        print(code)
        try:
            user.rfid_code = code
            user.save()
            return HttpResponse(content=json.dumps({
                'status': 'SUCCESS',
                'rfid_code': code,
                'user_pk': user.pk,
            }), content_type='application/json')
        except IntegrityError:
            print(code)
            return HttpResponse(content=json.dumps({
                'status': 'EXISTING',
            }), content_type='application/json')


def scan_profile(request):
    if request.method == "POST":
        code = request.POST.get('code').strip()
        code = re.sub(r'[\x00-\x1F]+', '', code)
        print(code)
        try:
            user = User.objects.get(rfid_code=code)
            return HttpResponse(content=json.dumps({
                'status': 'SUCCESS',
                'name': f"{user.first_name} {user.last_name}",
                'email': user.email,
                'appointment': user.appointment,
                'phone_number': user.phone_number,
                'address': user.address,
                'user_pk': user.pk,
                'photo': (user.photo.url if user.photo else "/media/image/avatar.png"),

            }), content_type='application/json')
        except ObjectDoesNotExist:
            return HttpResponse(content=json.dumps({
                'status': 'NoUser',
            }), content_type='application/json')

    return render(request, 'scan-profile.html')
