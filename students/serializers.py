from dataclasses import fields
from rest_framework import serializers
from students.models import Student, Study_Type, Study_Specialize


class StudyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study_Type
        fields = '__all__'

class StudySpecializeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study_Specialize
        fields = '__all__'

class Studentseializers(serializers.ModelSerializer):
    # study_type_id = StudyTypeSerializer()
    # study_specialize_id = StudySpecializeSerializer()
    study_type = serializers.CharField(source='study_type_id.study_type',read_only=True)
    study_specialize = serializers.CharField(source='study_specialize_id.study_specialize', read_only=True)
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'term_no',
            'student_code',
            'overall_rating',
            'study_type_id',
            'study_type',
            'study_specialize_id',
            'study_specialize',
            'email',
            'mobile',
            'national_id',
            ]



