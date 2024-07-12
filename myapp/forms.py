from django import forms
from .models import ArticleElon, ArticleNews, ArticleQabul2024

class ArticleElonForm(forms.ModelForm):
    class Meta:
        model = ArticleElon
        fields = [
            'title', 'title_en', 'title_ru', 
            'body', 'body_en', 'body_ru', 
            'img', 'img1', 'img2', 'img3'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_en': forms.TextInput(attrs={'class': 'form-control'}),
            'title_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'body_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'body_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ArticleNewsForm(forms.ModelForm):
    class Meta:
        model = ArticleNews
        fields = [
            'title', 'title_en', 'title_ru', 
            'body', 'body_en', 'body_ru', 
            'img', 'img1', 'img2', 'img3'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_en': forms.TextInput(attrs={'class': 'form-control'}),
            'title_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'body_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'body_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class Qabul24Form(forms.ModelForm):
    class Meta:
        model = ArticleQabul2024
        fields = ['file1','file2','file3','file4','file5' ]
        widgets = {
            'file1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file4': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file5': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
