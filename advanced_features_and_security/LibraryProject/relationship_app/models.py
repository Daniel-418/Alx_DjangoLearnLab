from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.utils import choices

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Book(models.Model):
    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change a book entry"),
            ("can_delete_book", "Can delete a book in the database")
        ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=(models.CASCADE))

    def __str__(self):  #pyright: ignore
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):  #pyright: ignore
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.PROTECT)

    def __str__(self):  #pyright: ignore
        return self.name

class UserProfile(models.Model):
    role_choices = [("Admin", "Admin"), ("Librarian", "Librarian"), ("Member", "Member")]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=role_choices)


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

