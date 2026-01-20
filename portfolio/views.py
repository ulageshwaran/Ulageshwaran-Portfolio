from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Skill, Experience, Certification, Achievement

def index(request):

    context = {
        'projects': Project.objects.all().order_by('-created_at'),
        'skills': {
            'frontend': Skill.objects.filter(category='FRONTEND'),
            'backend': Skill.objects.filter(category='BACKEND'),
            'tools': Skill.objects.filter(category='TOOLS'),
            'other': Skill.objects.filter(category='OTHER'),
        },
        'experiences': Experience.objects.all(),

        'certifications': Certification.objects.all(),
        'achievements': Achievement.objects.all(),
    }
    return render(request, 'home.html', context)
