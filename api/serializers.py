from rest_framework import serializers
from .models import Patient, Doctor, Mapping

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'created_at')

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'created_at')

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = '__all__'
        read_only_fields = ('id', 'assigned_at')
