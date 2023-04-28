from django import forms
from app.models import *

class EmployeeForm(forms.ModelForm):
    class meta:
        models=Employee
        fields= '__all__'