from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:  # validating email
            raise ValueError('EMAIL IS REQUIRED!!')
        if not username:  # validating username
            raise ValueError('USERNAME IS REQUIRED!!')

        email = self.normalize_email(email)  # normalizing the email
        user = self.model(email=email, username=username)  # creating user
        user.set_password(password)  # making the password hashed
        user.save(using=self._db)  # saving the user object

        return user

    """
    Function for creation of a superuser
    """

    def create_superuser(self, email, username, password):

        user = self.create_user(email=email, username=username, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = UserProfileManager()  # user profile context manager for interfacing with the database query operations

    USERNAME_FIELD = 'email'  # overriding the username field and using the email field for authentication
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = ['username']  # A list of Fields that are required for user creation

    ''' Creating s string representation of a user '''
    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)
