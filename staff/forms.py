from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import ContactUsModel


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'id': 'user_email',
            'placeholder': 'EMAIL'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'user_password',
            'placeholder': 'PASSWORD'
        })
    )


class ContactUsForm(forms.ModelForm):

    name = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'id': 'feedback_name',
            'placeholder': 'NAME'
        })
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'id': 'feedback_email',
            'placeholder': 'EMAIL'
        })
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'feedback_phone',
            'placeholder': 'PHONE NUMBER'
        })
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'id': 'feedback_message',
            'placeholder': 'Your text here...',
            'cols': '82',
            'rows': '5'
        })
    )

    class Meta:
        model = ContactUsModel
        fields = ['name', 'email', 'phone_number', 'text']


class AddStaffForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'user_password',
            'placeholder': 'PASSWORD'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password']
