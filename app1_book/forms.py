from django import forms 
from .models import *

class ImageForm(forms.ModelForm): 
    class Meta: 
        model = Number_store
        fields = ['num', 'topic','photo'] 

class AudioForm(forms.ModelForm):
    class Meta:
        model=Audio_storee
        fields=['record']