from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from applications.models import Application, Cycle, Stage, Cycle_Stage_Link, CycleStageRoute, PostponeCourseDocument


class Applicationseializers(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student_id.name', read_only=True)
    employee_name = serializers.CharField(source='current_employee_id.emp_name', read_only=True)
    current_stage = serializers.CharField(source='current_cycle_stage_link_id.cycle_id.cycle_name', read_only=True)

    class Meta:
        model = Application
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class CycleStageLinkSerializer(serializers.ModelSerializer):
    # cycle_name = serializers.CharField(source='cycle_id.cycle_name',read_only=True)
    # stage_id = StageSerializer(many=True)
    # stage_name = serializers.CharField(source='stage_id.stage_name',read_only=True)
    class Meta:
        model = Cycle_Stage_Link
        fields = [
            # 'cycle_id',
            'id',
            'stage_id',

        ]
        depth = 3


class CycleSerializer(serializers.ModelSerializer):
    # stages = serializers.StringRelatedField(many=True, read_only=True)
    stages = CycleStageLinkSerializer(many=True)

    class Meta:
        model = Cycle
        fields = [
            'cycle_name',
            'stages'
        ]
        depth = 3


class CycleStageRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleStageRoute
        fields = '__all__', ''
        depth = 1


class PostponeCourseSerializer(serializers.ModelSerializer):
    application_id = Applicationseializers()

    class Meta:
        model = PostponeCourseDocument
        fields = '__all__'
