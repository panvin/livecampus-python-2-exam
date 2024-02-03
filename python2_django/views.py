from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .utils import generate_random_string
from .forms import SessionForm
from .models import SessionSurvey
from .models import SurveyAnswer

@login_required
def session_list(request):
    sessionSurvey = SessionSurvey.objects.all()
    return render(request, 'session/session_list.html', {'sessionsurvey' : sessionSurvey})

@login_required
def session_create(request):
    
    currentUserInit = request.user
    urlInit = generate_random_string(8)
    dateStartedInit = datetime.now()
    dateEndInit = datetime.now() + timedelta(hours=3)
    context ={} 
  
    # Dictionnaire pour initialiser les données du formulaire 
    initialValues = { 
        "createdBy" : currentUserInit, 
        "url" : urlInit, 
        "dateStarted": dateStartedInit.strftime("%Y-%m-%dT%H:%M"), 
        "dateEnd": dateEndInit.strftime("%Y-%m-%dT%H:%M")
    }

    print(initialValues) 
    
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('session_list')
    else:
        form = SessionForm(initial = initialValues)
    return render(request, 'session/session_create.html', {'form' : form})

@login_required
def session_delete(request, id):
    sessionToDelete = get_object_or_404(SessionSurvey, id=id)
    if sessionToDelete:
        sessionToDelete.delete()

    sessionSurvey = SessionSurvey.objects.all()
    return render(request, 'session/session_list.html', {'sessionsurvey' : sessionSurvey})

def home_display(request):
    return render(request, 'home.html')