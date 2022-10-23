from django.shortcuts import render, redirect, reverse
from apps.users.models import User


def admin_list(request):
    admins = User.objects.all()
    return render(request, 'users.html', {'admins': admins})


def register_admin(request):
    if request.method == "POST":
        first_mame = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_admin = User.objects.create_user(email=email, username=username, password=password)
        new_admin.first_name = first_mame
        new_admin.last_name = last_name

        new_admin.save()

        # if 'success' in request.session:
        #     del request.session['success']
        # request.session['success'] = True

        return redirect(reverse(admin_list))

    return render(request, 'register-admin.html')
