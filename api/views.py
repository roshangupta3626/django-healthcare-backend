from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Patient, Doctor, Mapping
from .serializers import PatientSerializer, DoctorSerializer, MappingSerializer
from .permissions import IsOwnerOrReadOnly

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # only the patients created by this user
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Doctor.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Mapping.objects.all()

    def create(self, request, *args, **kwargs):
        # basic validation: patient belongs to user (optional)
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def doctors_for_patient(self, request, patient_id=None):
        mappings = Mapping.objects.filter(patient__id=patient_id)
        doctors = [m.doctor for m in mappings]
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
