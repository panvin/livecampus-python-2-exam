from django.contrib import admin
from .models import SessionSurvey, SurveyAnswer

admin.site.register(SessionSurvey)
admin.site.register(SurveyAnswer)