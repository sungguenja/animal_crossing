from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','nickname']
        labels = {
            'username': ('아이디'),
            'nickname': ('별명'),
            'password1': ('비밀번호'),
            'password2': ('비밀번호확인')
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class':'col-12 form-control', 'placeholder':'100자까지만 입력이 가능합니다'}),
            'nickname': forms.TextInput(attrs={'class':'col-12 form-control', 'placeholder':'익명이라고 정하시면 아무도 당신의 프로필을 못봅니다'}),
            'password1': forms.TextInput(attrs={'class':'col-12 form-control'}),
            'password2': forms.TextInput(attrs={'class':'col-12 form-control'})
        }
        help_texts = {
            'nickname': ('익명이라고 정하시면 아무도 당신의 프로필을 못봅니다')
        }