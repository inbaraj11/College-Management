from django.shortcuts import render
from rest_framework.decorators import api_view,  permission_classes
from rest_framework import generics
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from clgeapp.models import *
from clgeapp.serializers import *
from clgeapp.permissions import *
from django.contrib.auth.models import User


class CollegeList(generics.ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CollegeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class RegulationViewSet(viewsets.ModelViewSet):
    queryset = Regulation.objects.all()
    serializer_class = RegulationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStaffUser]


class StaffUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StaffUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUser]


class StudentUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStaffUser]


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStaffUser]

    # def get_queryset(self):
    #     return Marks.objects.filter(student__user=self.request.user)


class RankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = RankSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, IsStudentUser]

    def get_queryset(self):
        return Marks.objects.filter(student__user=self.request.user)


# @permission_classes([permissions.IsAuthenticatedOrReadOnly, IsAdminUser, IsOwnerOrReadOnly])
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'role': reverse('role-list', request=request, format=format),
        'department': reverse('department-list', request=request, format=format),
        'year': reverse('year-list', request=request, format=format),
        'section': reverse('section-list', request=request, format=format),
        'semester': reverse('semester-list', request=request, format=format),
        'batch': reverse('batch-list', request=request, format=format),
        'regulation': reverse('regulation-list', request=request, format=format),
        'subject': reverse('subject-list', request=request, format=format),
        'staff': reverse('staff-list', request=request, format=format),
        'student': reverse('student-list', request=request, format=format),
        'staffuser': reverse('staffuser-list', request=request, format=format),
        'studentuser': reverse('user-list', request=request, format=format),
        'mark': reverse('marks-list', request=request, format=format),
        'rank': reverse('rank-list', request=request, format=format),

    })