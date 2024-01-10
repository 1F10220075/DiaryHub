from django import forms
from .models import Diary

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索', max_length=100)

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content', 'author', 'category')
