from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SessionSurvey
from .models import SurveyAnswer

@login_required
def session_list(request):
    sessionSurvey = SessionSurvey.objects.all()
    return render(request, 'session/session_list.html', {'sessionsurvey' :sessionSurvey})

def home_display(request):
    return render(request, 'home.html')