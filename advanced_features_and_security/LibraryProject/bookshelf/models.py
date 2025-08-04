from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


#Custom User
class MyUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

#User manager
class MyUserManager(BaseUserManager):
    def create_user(self, username, date_of_birth, profile_photo):
        user = self.model(username=username, date_of_birth=date_of_birth,
                          profile_photo=profile_photo)
        user.save()
        return user
