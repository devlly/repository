from django.db import models

class Developers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=30)
    

class Education(models.Model):
    university =  models.CharField(max_length=50)
    year_of_graduation = models.IntegerField()
    developers = models.ManyToManyField(Developers, related_name='education')


class Empl_history(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    fr = models.DateField(verbose_name='from')
    to = models.DateField()
    developers = models.ManyToManyField(Developers, related_name='employment_history')


class Skills(models.Model):
    SKILLS_CHOICES = (
    ('p', 'Python'),
    ('d',  'Django'),
    ('drf', 'Django Rest Framework'),
    )
    skills_choices = models.CharField(max_length=2, default='', choices=SKILLS_CHOICES,)
    other_skills = models.CharField(max_length=100, verbose_name='other skills')
    developers = models.ManyToManyField(Developers, related_name='skills')
