from django.shortcuts import render

from random import randint

from slow_loris.core.models import Suggestion, Intro
from slow_loris.core.forms import SuggestionForm
from slow_loris.settings import MAX_FLAGS

def submit(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            # update db here
            s = Suggestion()
            text = form.cleaned_data['text']
            if text[-1] == '?':
                text = text[0:-1]
            s.text = text
            s.link = form.cleaned_data['link']
            s.save()
            
            newform = SuggestionForm()
            return render(request, 'submit.html', {
                'thanks': True, 'form': newform,
            })
    else:
        form = SuggestionForm()
    
    return render(request, 'submit.html', {
        'thanks': False, 'form': form,
    })
        
def home(request):
    intro_count = Intro.objects.count()
    intro = Intro.objects.all()[randint(0, intro_count - 1)]
    
    suggestions = Suggestion.objects.filter(flag__lte=MAX_FLAGS)
    suggestion_count = suggestions.count()
    suggestion = suggestions[randint(0, suggestion_count - 1)]
    
    return render(request, 'home.html', {
        'intro': intro,
        'suggestion': suggestion,
    })
