from django.contrib import admin
from .models import Project, Skill, Experience, Tag, ContactMessage, Education, Certification, Achievement

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    filter_horizontal = ('tags',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'is_current')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'duration')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('event', 'position', 'date')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

admin.site.register(Tag)
