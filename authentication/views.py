from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt

from .forms import RegistrationForm
from main.models import Customer


# ? Login and Logout is a Auto feature in Django

# Create your views here.
@csrf_exempt
def signup(request):
    message = ""
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Customer.objects.create(user=user)
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "registration/sign_up.html", context)
