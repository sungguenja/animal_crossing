from django import forms
from .models import *

class Radish_Form(forms.ModelForm):
    class Meta:
        model = Radish
        fields = ['end','lock','bell']
        labels = {
            'end': ('언제까지 열어두시나요?'),
            'lock': ('비밀번호'),
            'bell': ('구조대의 가격은?')
        }
        widgets = {
            'end': forms.widgets.DateTimeInput(format=["%Y-%m-%d %H:%M:%S"],attrs={'class':'form-control','placeholder':"'년-월-일 시:분:초' 형태로 입력해주세요"}),
            'lock':  forms.TextInput(attrs={'class':'form-control', 'placeholder': '비밀번호를 입력해주세요'}),
            'bell': forms.TextInput(attrs={'class':'form-control', 'placeholder': '숫자만 입력해주세요'})
        }

class Article_Form(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category','title','want','calling']
        labels = {
            'category': ('물건의 종류'),
            'title': ('어떤 것을 파시나요?'),
            'want': ('원하시는 것은 무엇인가요?'),
            'calling': ('연락처')
        }
        widgets = {
            'category': forms.Select(choices=[['artwork','예술품'],['dress','옷'],['diy','diy레시피'],['fossil','화석'],['fruit','과일'],['flower','낮은나무 또는 꽃'],['material','재료'],['villager','주민'],['service','서비스'],['tool','도구'],['other','기타']],attrs={'class':'btn btn-outline-dark dropdown-toggle col-12'}),
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'어떤 것을 파시나요? 아니면 어떤 서비스를 제공해주시나요?'}),
            'want': forms.TextInput(attrs={'class':'form-control','placeholder':'가격 또는 어떤 것을 적어주세요'}),
            'calling': forms.TextInput(attrs={'class':'form-control','placeholder':'메신저와 메신저 아이디를 입력해주세요 (ex. 디스코드 #디스코드코드)'})
        }