from django import forms
from django.db import models
from slow_loris.core.models import Suggestion

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        exclude = 'flag'