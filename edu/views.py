from django.shortcuts import get_object_or_404,render

from django.http import HttpResponse
from .models import Project,Student


def home(request):
    return HttpResponse("<h1>Hello, from Communication Engineering</h1><br><h2>Tishreen University</h2>")
        


def projects(request):
    projects = Project.objects.all()
    return render(request, 'edu/projects.html', {'projects': list(projects)})
    
def students(request):
    students = Student.objects.all()
    return render(request, 'edu/students.html', {'students': list(students)})