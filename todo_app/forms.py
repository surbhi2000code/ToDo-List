from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'palceholder':'Add new task...'}))
    class Meta:
        model = drone
        fields = ('title','complete')