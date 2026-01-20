from django.contrib import admin
from .models import Project, Skill, Experience, Tag, Certification, Achievement

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


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'date')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('event', 'position', 'date')


admin.site.register(Tag)
