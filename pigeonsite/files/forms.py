from django import forms
from .models import UploadedFile
from django.db import models

# Create your models here.

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
