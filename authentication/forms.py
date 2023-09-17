from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}), label="Confirm Password")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
