from django.shortcuts import redirect, render
from .models import *

# updated file
default_data = {
    'app_name': 'My Resume'
}

# Create your views here.

# load personal info
def load_personal_info():
    default_data['personal_info'] = User.objects.all()[::-1]

# load all skills
def load_skills():
    default_data['skills'] = Skill.objects.all()[::-1]

def index(request):
    load_personal_info()
    load_skills()
    return render(request, 'index.html', default_data)

# show resume page
def resume_page(request):
    return render(request, 'resume.html', default_data)

# register page
def register_page(request):
    return render(request, 'register_page.html', default_data)

# register functionality
def register(request):
    if request.method == 'POST':
        master = Master.objects.create(
            Email=request.POST['email'],
            Password=request.POST['password'],
            IsActive = True
        )

        User.objects.create(Master=master)

        return redirect(register_page)
    else:
        return redirect(register_page)

# login page
def login_page(request):
    return render(request, 'login_page.html', default_data)

# login functionality
def login(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.POST['email'])

        if request.POST['password'] == master.Password:
            request.session['email'] = request.POST['email']
            
        return redirect(profile_page)
    else:
        return redirect(profile_page)

# load profile data
def profile_data(request):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)
    
    education = Education.objects.filter(User = user)[::-1]
    experience = Experience.objects.filter(User = user)[::-1]
    skills = Skill.objects.filter(User = user)[::-1]
    languages = Language.objects.filter(User = user)[::-1]

    default_data['user_data'] = {
        'user': user,
        'education': education,
        'skills': skills,
        'languages': languages,
        'experience': experience
    }

# profile page
def profile_page(request):
    profile_data(request)
    return render(request, 'profile_page.html', default_data)

# update profile
def update_profile(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)

        user.FullName = request.POST['FullName']
        user.JobProfile = request.POST['JobProfile']
        user.Mobile = request.POST['Mobile']
        user.Gender = request.POST['Gender']
        user.Address = request.POST['Address']

        if 'profile_pic' in request.FILES:
            user.ProfilePic = request.FILES['profile_pic']

        user.save()

        return redirect(profile_page)
    else:
        pass

# update education
def update_education(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)
        education = Education()

        education.User = user
        education.Board = request.POST['Board']
        education.Standard = request.POST['Standard']
        education.StartDate = request.POST['StartDate']
        education.EndDate = request.POST['EndDate']
        education.IsContinue = True if 'IsContinue' in request.POST else False

        education.save()

        return redirect(profile_page)
    else:
        pass

# update language
def update_language(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)
        language = Language()

        language.User = user
        language.LangName = request.POST['language']
        language.Level = request.POST['level']
        language.save()

        return redirect(profile_page)
    else:
        pass

# remove education
def remove_language(request, pk):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    Language.objects.get(User=user, pk=pk).delete()

    return redirect(profile_page)

# remove education
def remove_education(request, pk):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    Education.objects.get(User=user, pk=pk).delete()

    return redirect(profile_page)

# logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(index)