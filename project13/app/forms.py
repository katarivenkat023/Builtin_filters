from django import forms
g=(('MALE','male'),('FEMALE','female'))
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea)
    gender=forms.ChoiceField(choices=g)