from django import forms
from .import models

class CreatePost(forms.ModelForm):
    class Meta:
        model=models.Post # class name of models
        fields=["title","banner","slug","body"]
        