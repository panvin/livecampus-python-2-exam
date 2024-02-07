from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

class SessionSurvey(models.Model):
    name         = models.CharField(max_length=50)
    status       = models.BooleanField(default=False)
    createdBy    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dateStarted  = models.DateTimeField()
    dateEnd      = models.DateTimeField()
    url          = models.CharField(max_length=250, unique=True)

class SurveyAnswer(models.Model):
    
    class ExerciceDifficulty(models.TextChoices):
        EASY     = 'EA', _('Facile')
        NORMAL   = 'NO', _('OK')
        HARD     = 'HA', _('Un peu compliqué')
        VERYHARD = 'VA', _('Très compliqué')
        EXTREME  = 'EX', _('Au secours')

    class ExerciceProgression(models.TextChoices):
        ACQUIRED       = 'AC', _('J\'ai compris')
        INPROGRESS     = 'IP', _('Je dois encore pratiquer')
        NOTYETACQUIRED = 'NA', _('C\'est flou')
    
    session         = models.ForeignKey(SessionSurvey, on_delete=models.CASCADE)
    student         = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    percentage      =  models.SmallIntegerField(default=0)
    progression     = models.CharField( max_length=2, choices=ExerciceProgression.choices, default=ExerciceProgression.NOTYETACQUIRED)
    difficulty      = models.CharField( max_length=2, choices=ExerciceDifficulty, default=ExerciceDifficulty.EXTREME)
    dateSend        = models.DateTimeField()
    dateInitialSend = models.DateTimeField()