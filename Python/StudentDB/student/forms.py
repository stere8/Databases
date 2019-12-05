from django import forms
from .models import Student


class AddStudentForm(forms.ModelForm):
    # The below code is not needed since we already have a form
    # name = forms.CharField(label="Student's name", max_length=60)
    # surname = forms.CharField(label="Student's surname", max_length=60)
    # age = forms.IntegerField(label="Age", max_length=3)
    # year = forms.IntegerField(label="Year of study", max_length=1)
    # year_of_graduation = forms.IntegerField(label="Year of graduation ", max_length=4)
    class Meta:
        model = Student
        fields = ["name", "surname","major", "age", "year", "year_of_graduation"]
