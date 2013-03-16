from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_POST

from core.models import Suggestion, Intro, Picture
from core.forms import SuggestionForm
from settings import MAX_FLAGS

def get_random(my_model, filter=False, limit='', criterion=''):
    from random import randint
    
    if filter:
        my_queryset = my_model.objects.filter(**{limit + '__lte' : criterion})
    else:
        my_queryset = my_model.objects.all()
    
    count = my_queryset.count()
    try:
        return my_queryset.all()[randint(0, count - 1)]
    except:
        """
        make sure to seed the db with something you trust is good
        even if users flag it
        """
        return my_model.objects.filter(pk=1)[0]

def submit(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
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
    intro = get_random(Intro)
    suggestion = get_random(Suggestion,
        filter=True,
        limit='flag', 
        criterion=MAX_FLAGS
    )
    picture = get_random(Picture)
    
    return render(request, 'home.html', {
        'intro': intro,
        'suggestion': suggestion,
        'picture': picture,
    })
    
def flag(request, suggestion_id):
    if request.is_ajax():
        suggestion = Suggestion.objects.get(pk=suggestion_id)
        suggestion.flag += 1
        suggestion.save()
        return HttpResponse("suggestion flagged")
    else:
        raise Http404

def review(request):
    if request.user.is_staff:
        flagged_suggestions = Suggestion.objects.filter(flag__gte=MAX_FLAGS).order_by('-flag')
        return render(request, 'review.html', {
            'flagged_suggestions': flagged_suggestions
        })
    else:
        raise Http404
