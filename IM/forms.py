from django import forms
from .models import Reservation,announcement

class announcementForm(forms.ModelForm):
    class Meta:
        model = announcement
        fields = ['text']
        labels = {'text': 'announcement:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['name','age','date']
        