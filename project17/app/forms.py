from django import forms
from app.models import *
# create your forms here
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'