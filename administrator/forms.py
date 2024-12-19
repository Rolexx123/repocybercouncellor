from django.forms import ModelForm
from .models import *


class complaint_form(ModelForm):
    class Meta:
        model=complaint
        fields=['complaint','replay']

class councellor_form(ModelForm):
    class Meta:
        model=Councellor
        fields=['name','age','gender','address','phone','email','qualification']
 
