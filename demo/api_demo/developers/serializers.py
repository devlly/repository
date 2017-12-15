from rest_framework import serializers
from .models import *

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empl_history
        fields = ('company', 'role', 'fr', 'to')

class EduSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('university', 'year_of_graduation')

class SkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('skills_choices', 'other_skills')


class DevSerializer(serializers.ModelSerializer):
    skills = SkSerializer(many=True)
    employment_history = EmpSerializer(many=True)
    education = EduSerializer(many=True)

    class Meta:
        model = Developers
        fields = ('name', 'surname', 'skills', 'education', 'employment_history')


#
# data = {
#     'name': 'Tom',
#     'Surname': 'DangerMouse',
#     'skills' : ['Python', 'Django'],
#     'employment_history' : [
#         {'copmany' : 'Jemset', 'role' : 'developer', 'from' : '', 'to' : ''},
#     ],
#     'education' : [
#         {'university': 'CSbGU', 'year_of_graduation': ''},
#     ],
# }
# serializer = DevSerializer(data=data)
# serializer.is_valid()
# serializer.save()
