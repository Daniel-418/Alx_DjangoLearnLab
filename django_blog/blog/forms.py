from django.contrib.auth import forms as userform, get_user_model, models
from django import forms

class CustomUserCreationForm(userform.UserCreationForm):
    email = forms.EmailField(required=True)
    bio = forms.Textarea()

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "bio", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "bio"]
