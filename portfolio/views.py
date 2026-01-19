from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Skill, Experience, ContactMessage, Education, Certification, Achievement

def index(request):
    if request.method == 'POST':
        # Simple AJAX handler for contact form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
        return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)

    context = {
        'projects': Project.objects.all().order_by('-created_at'),
        'skills': {
            'frontend': Skill.objects.filter(category='FRONTEND'),
            'backend': Skill.objects.filter(category='BACKEND'),
            'tools': Skill.objects.filter(category='TOOLS'),
            'other': Skill.objects.filter(category='OTHER'),
        },
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certifications': Certification.objects.all(),
        'achievements': Achievement.objects.all(),
    }
    return render(request, 'home.html', context)
