from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.userprofile.role == "Admin"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, template_name="relationship_app/admin_view.html")
