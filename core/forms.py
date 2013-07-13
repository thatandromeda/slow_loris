from django import forms
from django.db import models
from core.models import Suggestion

class SuggestionForm(forms.ModelForm):
    text = forms.CharField(label='How about you...')
    link = forms.URLField(label='Link for next steps')
    captcha = forms.CharField(label="Prove you're not a spammer! What's the 2013 location of LITA Forum?")
    
    class Meta:
        model = Suggestion
        exclude = 'flag'
        
    def clean_captcha(self):
        data = self.cleaned_data['captcha'].lower()
        if 'louisville' not in data:
            raise forms.ValidationError("Whoops, that's not where Forum is.")
        