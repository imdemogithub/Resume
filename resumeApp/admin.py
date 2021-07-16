from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *

# Register your models here.
class SuperAdmin(admin.ModelAdmin):
    admin.site.site_title = admin.site.site_header = 'Resume Maker'
    list_per_page = 5

class MasterHeader(SuperAdmin):
    model = Master
    list_display = ('id', 'Email', 'IsActive')

class UserHeader(SuperAdmin):
    model = User
    list_display = ('id', 'FullName', 'Gender', 'Mobile')
    list_filter = ('JobProfile', 'Gender')

class SkillHeader(SuperAdmin):
    model = Skill
    list_display = list_filter = ('Skill', 'Level')

class ExperienceHeader(SuperAdmin):
    model = Experience
    list_display = list_filter = ('JobProfile', 'IsContinue')

class EducationHeader(SuperAdmin):
    model = Education
    list_display = list_filter = ('Board', 'Standard', 'IsContinue')

class LangHeader(SuperAdmin):
    model = Language
    list_display = list_filter = ('LangName', 'Level')

list_models = [
    MasterHeader, UserHeader, SkillHeader, EducationHeader, LangHeader, ExperienceHeader,
]

for lm in list_models:
    admin.site.register(lm.model, lm)