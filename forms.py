from django import forms
from .models import Course
from .models import Instructor


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']  # Adjust fields as per your Course model

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'email', 'bio']