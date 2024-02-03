from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import SessionForm
from .models import SessionSurvey
from .models import SurveyAnswer

@login_required
def session_list(request):
    sessionSurvey = SessionSurvey.objects.all()
    return render(request, 'session/session_list.html', {'sessionsurvey' : sessionSurvey})

@login_required
def session_create(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('session_list')
    else:
        form = SessionForm()
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