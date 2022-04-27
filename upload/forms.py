from django import forms
from .models import FileName

class FileNameForm(forms.ModelForm):
    
    class Meta:
        model = FileName
        fields = '__all__'
