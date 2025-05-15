from django.contrib import admin
from .models import Course, Student, Registration
from .models import Instructor


admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(Instructor)