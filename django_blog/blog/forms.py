from django.contrib.auth import forms as userform, models
from django import forms

class CustomUserCreationForm(userform.UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = models.User
        fields = ["username", "email", "password1", "password2"]
