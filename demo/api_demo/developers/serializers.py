from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer


class UniSerializer(serializers.ModelSerializer):
    university = serializers.CharField()
    faculty = serializers.CharField()
    data_of_graduation = serializers.DateField()

    class Meta():
        model = University
        fields = (
            'university',
            'faculty',
            'data_of_graduation',
            )


class CourseSerializer(serializers.ModelSerializer):
    course = serializers.CharField()
    data_of_graduation = serializers.DateField()

    class Meta:
        model = Courses
        fields = ('course', 'data_of_graduation')


class EduSerializer(serializers.ModelSerializer):
    university = UniSerializer()
    course = CourseSerializer()

    class Meta:
        model = Education
        fields = ('university', 'course')


class CompanySerializer(serializers.ModelSerializer):
    company = serializers.CharField()
    role = serializers.CharField()
    fr = serializers.DateField()
    to = serializers.DateField()

    class Meta:
        model = Company
        fields = ('company', 'role', 'fr', 'to')


class EmpSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Empl_history
        fields = ('company', )


class SkSerializer(serializers.ModelSerializer):
    skills = serializers.CharField()

    class Meta:
        model = Skills
        fields = ('skills', )


class DevSerializer(WritableNestedModelSerializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    skills = SkSerializer(many=True)
    employment_history = EmpSerializer(many=True)
    education = EduSerializer(many=True)

    class Meta:
        model = Developers
        fields = (
            'name',
            'surname',
            'skills',
            'employment_history',
            'education',
            )

#     skills = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Developers
#         fields = ('name', 'surname', 'skills', 'education', 'employment_history')
