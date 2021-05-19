from rest_framework import serializers, fields
from clgeapp.models import *
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


# class UserSerializer(serializers.ModelSerializer):
#     # college = serializers.PrimaryKeyRelatedField(many=True, queryset=College.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username',]

class StaffUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()

        return user


class StudentUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    # student = serializers.HyperlinkedRelatedField(many=True, view_name='student-detail', read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class CollegeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = College
        fields = ['id', 'name', 'code', 'college_status', 'address', 'owner']


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ['id', 'name', 'code',]


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name', 'code',]


class YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Year
        fields = ['id', 'name', 'code',]


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ['id', 'name', 'code',]


class SemesterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Semester
        fields = ['id', 'name', 'code',]


class BatchSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Batch
        fields = ['id', 'start_year', 'end_year', 'owner']


class RegulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regulation
        fields = ['id', 'year',]

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['name', 'sub_code', 'dept', 'semester', 'Regulation']

class StaffSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedIdentityField(many=True, view_name='user-detail', format='html')
    class Meta:
        model = Staff
        fields = ['user', 'name', 'address', 'employee_id', 'email', 'mobile_num', 'role', 'dept', 'subject',
                  'Active', 'Staff_status', 'Superuser_status']


class StudentSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    # mark = serializers.HyperlinkedRelatedField(view_name='marks-detail', read_only=True)
    class Meta:
        model = Student
        fields = ['user', 'name', 'address', 'register_id', 'email', 'dept', 'year', 'section', 'semester',
                  'batch', 'regulation', 'Active', 'Staff_status', 'Superuser_status']

class MarkSerializer(serializers.ModelSerializer):
    # student = serializers.HyperlinkedIdentityField(view_name='student-details', read_only=True)
    class Meta:
        model = Marks
        fields = ['mark', 'student', 'subject']

class RankSerializer(serializers.ModelSerializer):
    # student = serializers.HyperlinkedIdentityField(view_name='student-details', read_only=True)
    class Meta:
        model = Marks
        fields = ['mark', 'subject']

    def to_representation(self, instance):
        return {
            'mark': instance.mark,
            'subject': instance.subject.name,
        }