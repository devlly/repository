from django.db import models

class Skills(models.Model):
    skills = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Developers(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    skills = models.ManyToManyField(
        Skills,
        related_name='developers',
        )

    class Meta:
        verbose_name = 'Developer'
        verbose_name_plural = 'Developers'


class University(models.Model):
    university =  models.CharField(max_length=100)
    faculty = models.CharField(max_length=50)
    data_of_graduation = models.DateField()

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'


class Courses(models.Model):
    course = models.CharField(max_length=50)
    data_of_graduation = models.DateField()

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Education(models.Model):
    developers = models.ManyToManyField(
        Developers,
        related_name='education',
        )

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        blank=True,
        )

    course = models.ForeignKey(
        Courses,
        on_delete=models.CASCADE,
        blank=True,
        )

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'


class Company(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=30)
    fr = models.DateField(verbose_name='from')
    to = models.DateField()

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Empl_history(models.Model):
    developers = models.ManyToManyField(
        Developers,
        related_name='employment_history',
        )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=True,
        )

    class Meta:
        verbose_name = 'Employment history'
        verbose_name_plural = 'Employment history'





    #other_skills = models.CharField(max_length=100, verbose_name='other skills')
