from django import forms
from django.db import models
from core.models import Suggestion

class SuggestionForm(forms.ModelForm):
    text = forms.CharField(label='How about you...')
    link = forms.URLField(label='Link for next steps')
    
    class Meta:
        model = Suggestion
        exclude = 'flag'