from django.db import models

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(max_length=25, unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)

    def __str__(self):
        return self.Email

gender = (
    ('m', 'Male'),
    ('f', 'Female'),
)

class User(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    ProfilePic = models.FileField(upload_to='users/', default='default.png')
    FullName = models.CharField(max_length=30, null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=gender)
    JobProfile = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=10, null=True, blank=True)
    Address = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'PersonalInfo'

class Skill(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Skill = models.CharField(max_length=50)
    Level = models.CharField(max_length=3)

    class Meta:
        db_table = 'Skill'

class Experience(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    JobProfile = models.CharField(max_length=30)
    StartDate = models.DateField(auto_created=True)
    EndDate = models.DateField(auto_created=False, default='2021-06-01')
    IsContinue = models.BooleanField(default=False)

    class Meta:
        db_table = 'Experience'

class Education(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Board = models.CharField(max_length=30)
    Standard = models.CharField(max_length=20)
    StartDate = models.DateField(auto_created=True)
    EndDate = models.DateField(auto_created=False, default='2021-06-01')
    IsContinue = models.BooleanField(default=False)

    class Meta:
        db_table = 'Education'

class Language(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    LangName = models.CharField(max_length=30)
    Level = models.CharField(max_length=3)

    class Meta:
        db_table = 'Language'