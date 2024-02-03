from django import forms
from .models import SessionSurvey

class SessionForm(forms.ModelForm):
    class Meta:
        model = SessionSurvey
        fields = ['name', 'createdBy','dateCreation', 'dateEnd', 'url']
        widgets = {
            'dateCreation': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dateEnd': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

