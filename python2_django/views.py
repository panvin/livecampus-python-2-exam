from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .utils import generateRandomString, getFormattedDateForHomePage, getPercentageAsStr
from .forms import SessionForm
from .models import SessionSurvey
from .models import SurveyAnswer

@login_required
def session_list(request):
    sessionSurvey = SessionSurvey.objects.filter(createdBy = request.user.id)

    return render(request, 'session/session_list.html', {'sessionsurvey' : sessionSurvey})

@login_required
def session_create(request):
    
    currentUserInit = request.user
    urlInit = generateRandomString(8)
    dateStartedInit = datetime.now()
    dateEndInit = datetime.now() + timedelta(hours=3)
    context ={} 
  
    # Dictionnaire pour initialiser les données du formulaire 
    initialValues = { 
        "createdBy" : currentUserInit.id, 
        "url" : urlInit, 
        "dateStarted": dateStartedInit, 
        "dateEnd": dateEndInit
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
def session_edit(request, id):
    sessionToEdit = get_object_or_404(SessionSurvey, id=id)

    if request.method == 'POST':
        form = SessionForm(request.POST, instance=sessionToEdit)
        if form.has_changed:
            if form.is_valid():
                form.save()
            return redirect('session_list')
    else:  
        form = SessionForm(instance=sessionToEdit)

    return render(request, 'session/session_edit.html', {'form' : form})

@login_required
def session_disable(request, id):
    sessionToDisable = get_object_or_404(SessionSurvey, id=id)
    if sessionToDisable:
        sessionToDisable.status = False
        sessionToDisable.save()

    return redirect(session_list)

@login_required
def session_enable(request, id):
    sessionToDisable = get_object_or_404(SessionSurvey, id=id)
    if sessionToDisable:
        sessionToDisable.status = True
        sessionToDisable.save()

    return redirect(session_list)

@login_required
def session_delete(request, id):
    sessionToDelete = get_object_or_404(SessionSurvey, id=id)
    if sessionToDelete:
        sessionToDelete.delete()

    return redirect(session_list)

@login_required
def answer_summary(request, id):
    listAnswers = SurveyAnswer.objects.filter(session=id)
    
    nbrStudents = listAnswers.count()

    return render(request, 'answer/summary.html')

def home_display(request):  
    context = {} 
    if request.user.is_authenticated:
        date = getFormattedDateForHomePage()
        surveyCount = SessionSurvey.objects.filter(createdBy = request.user.id, status = True).count()
        context = {
           'date' : date,
          'surveyCount' : str(surveyCount) 
        }

    return render(request, 'home.html', context)