from django.contrib.auth import forms as userform, get_user_model, models
from .models import Post
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

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("Title cannot be blank")
        return title

