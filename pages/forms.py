from django import forms
from .models import *

class Design_Form(forms.ModelForm):
    class Meta:
        model = design
        fields = ['title', 'design_img', 'category']