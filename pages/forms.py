from django import forms
from .models import *

class Design_Form(forms.ModelForm):
    class Meta:
        model = design
        fields = ['title', 'design_img', 'category']
        labels = {
            'title': ('제목'),
            'design_img': ('디자인'),
            'category': ('도안종류')
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': '제목을 적어주세요 100자까지가능합니다.'}),
            'category': forms.Select(choices=[['분류X','분류X'],['상의','상의'],['원피스','원피스'],['모자','모자']],attrs={'class':'btn btn-outline-dark dropdown-toggle col-12'})
        }