from django import forms
from django.utils.translation import gettext as _
from .utils import isDateBeforeNow, isFirstDateOlderThanSecond
from .models import SessionSurvey, SurveyAnswer

class SessionForm(forms.ModelForm):
    class Meta:
        model = SessionSurvey
        fields = ['name', 'dateStarted','dateEnd', 'url']
        widgets = {
            'dateStarted': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dateEnd'    : forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            "name"       : _("Nom de l'enquête"),
            "dateStarted": _("Date d'ouverture"),
            "dateEnd"    : _("Date de fermeture"),
            "url"        : _("Pattern pour URL"),
        }

    def clean(self):
 
        # On ajoute des éléments de validation à notre formulaire
        super(SessionForm, self).clean()
         
        dateEnd = self.cleaned_data.get('dateEnd')
        dateStarted = self.cleaned_data.get('dateStarted')
        url = self.cleaned_data.get('url')
 
        if len(url) < 8:
            self._errors['url'] = self.error_class([
                'Le pattern d\'url doit contenir au moins 8 caractères'])
        if isFirstDateOlderThanSecond(dateEnd, dateStarted) :
            self._errors['dateEnd'] = self.error_class([
                'La date de fin de l\'enquête ne peux pas être avant la date d\'ouverture '])
        if isDateBeforeNow(dateEnd) :
            self._errors['dateEnd'] = self.error_class([
                'La date de fin de l\'enquête ne peux pas être dans le passé'])
 
        # return any errors if found
        return self.cleaned_data