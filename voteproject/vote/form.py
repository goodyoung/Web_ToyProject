from django import forms
from main.models import Registration_title, Registration_article

class TitleForm(forms.ModelForm):
    class Meta:
        model = Registration_title
        fields = ['title']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Registration_article
        fields = ['article', 'count']
