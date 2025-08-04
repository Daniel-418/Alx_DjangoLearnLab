from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


#Custom User
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

#User manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, 
                    date_of_birth, profile_photo, **extra_fields):
        user = self.model(username=username, password=password,
                          date_of_birth=date_of_birth,
                          profile_photo=profile_photo, **extra_fields)
        user.save()
        return user

    def create_superuser(self, username, 
                         password, date_of_birth, 
                         profile_photo, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            username=username,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields)
