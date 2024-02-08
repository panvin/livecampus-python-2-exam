from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from datetime import datetime, timedelta
from .utils import generateRandomString, getFormattedDateForHomePage, generateJwt
from .forms import SessionForm
from .models import SessionSurvey, SurveyAnswer

# View pour la page d'acceuil du projet Django
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

# View permettant d'afficher la liste des sesssions d'enquête existante pour l'utilisateur
@login_required
@permission_required('python2_django.view_sessionsurvey', raise_exception=True)
def session_list(request):
    sessionSurvey = SessionSurvey.objects.filter(createdBy = request.user.id)
    baseUrl = request.build_absolute_uri()

    context = {
        'sessionsurvey' : sessionSurvey,
        'baseUrl' : baseUrl
    }

    return render(request, 'session/session_list.html', context)

# View de création de session d'enquête
@login_required
@permission_required('python2_django.add_sessionsurvey', raise_exception=True)
def session_create(request):
    
    currentUserInit = request.user
    urlInit = generateRandomString(8)
    dateStartedInit = datetime.now()
    dateEndInit = datetime.now() + timedelta(hours=3)
  
    # Dictionnaire pour initialiser les données du formulaire 
    initialValues = { 
        "createdBy" : currentUserInit.id, 
        "url" : urlInit, 
        "dateStarted": dateStartedInit, 
        "dateEnd": dateEndInit
    }    
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('session_list')
    else:
        form = SessionForm(initial = initialValues)

    context = {
        'form' : form
    }

    return render(request, 'session/session_create.html', context)

# View pour lédition de session d'enquêtes
@login_required
@permission_required('python2_django.change_sessionsurvey', raise_exception=True)
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

    context = {
        'form' : form
    }

    return render(request, 'session/session_edit.html', context)

# View utilisée pour changer l'état d'une session d'enquête
@login_required
@permission_required('python2_django.change_sessionsurvey', raise_exception=True)
def session_change_state(request, id):
    sessionToModify = get_object_or_404(SessionSurvey, id=id)
    if sessionToModify:
        sessionToModify.status = not sessionToModify.status
        sessionToModify.save()

    return redirect(session_list)

# View utilisée pour supprimer une session d'enquête
@login_required
@permission_required('python2_django.delete_sessionsurvey', raise_exception=True)
def session_delete(request, id):
    sessionToDelete = get_object_or_404(SessionSurvey, id=id)
    if sessionToDelete:
        sessionToDelete.delete()

    return redirect(session_list)

# View utilisée pour afficher les résultats de l'enquête
@login_required
@permission_required('python2_django.view_surveyanswer', raise_exception=True)
def answer_summary(request, id):
    listAnswers = SurveyAnswer.objects.filter(session=id)
    
    countStudents = listAnswers.count()
    countDifficulty = {
        'EA': listAnswers.filter(difficulty=SurveyAnswer.ExerciceDifficulty.EASY).count(),
        'NO': listAnswers.filter(difficulty=SurveyAnswer.ExerciceDifficulty.NORMAL).count(),
        'HA': listAnswers.filter(difficulty=SurveyAnswer.ExerciceDifficulty.HARD).count(),
        'VA': listAnswers.filter(difficulty=SurveyAnswer.ExerciceDifficulty.VERYHARD).count(),
        'EX': listAnswers.filter(difficulty=SurveyAnswer.ExerciceDifficulty.EXTREME).count()
    }
    countProgression ={
        'AC': listAnswers.filter(progression=SurveyAnswer.ExerciceProgression.ACQUIRED).count(),
        'IP': listAnswers.filter(progression=SurveyAnswer.ExerciceProgression.INPROGRESS).count(),
        'NA': listAnswers.filter(progression=SurveyAnswer.ExerciceProgression.NOTYETACQUIRED).count()
    }
    coutPercentage = {
        "BEGIN"    : listAnswers.filter(percentage__lte=33).count(),
        "MID"      : listAnswers.filter(percentage__gt=33, percentage__lte=66).count(),
        "NEAR"     : listAnswers.filter(percentage__gt=66, percentage__lt=100).count(),
        "FINISHED" : listAnswers.filter(percentage=100).count()

    }

    context = {
        'countstudents'    : countStudents,
        'countdifficulty'  : countDifficulty,
        'countprogression' : countProgression,
        'countpercentage'  : coutPercentage,
        'answers'          : listAnswers
    }

    return render(request, 'answer/summary.html', context)

# View utilisée pour afficher le formulaire de l'enquête
@login_required
@permission_required(['python2_django.add_surveyanswer', 'python2_django.change_surveyanswer'], raise_exception=True)
def answer_create_or_edit(request, urlPattern):
    
    currentUser = request.user
    currentSession = get_object_or_404(SessionSurvey, url=urlPattern)
    currentUserAnswers = SurveyAnswer.objects.filter(session=currentSession.id, student=currentUser.id)
    
    # Création du token JWTpour l'API Flask
    token = generateJwt(currentUser.id, currentUser.username, currentSession.id)
    
    # Initialisation des données du formulaire
    if not currentUserAnswers:
        progression = SurveyAnswer.ExerciceProgression.NOTYETACQUIRED
        difficulty  = SurveyAnswer.ExerciceDifficulty.NORMAL
        percentage  = 0
        
    else:
        progression = currentUserAnswers[0].progression
        difficulty  = currentUserAnswers[0].difficulty
        percentage  = currentUserAnswers[0].percentage
        
    data = {
        'fullname'   : f"{currentUser.first_name} {currentUser.last_name}",
        'progression': progression,
        'percentage' : percentage,
        'difficulty' : difficulty
    }

    # Récupération des l'URL de l'API dans les settings Django
    urlApi = settings.API_FLASK_URL
    context = {
        'answer' : data, 
        'urlApi': urlApi 
    }
        
    response = render(request, 'answer/survey.html', context)
    response.set_cookie("jwt", token, httponly=True)
    return response