from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


class BaseModel(models.Model):

    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class BaseModel2(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField()

    class Meta:
        abstract = True


class College(BaseModel, BaseModel2):

    STATUS = (
        ('naac', 'NAAC'),
        ('nba', 'NBA'),
        ('none', 'NONE'),
    )
    college_status = MultiSelectField(choices=STATUS,
                                      max_choices=2,
                                      max_length=10
    )
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(BaseModel, BaseModel2):
    pass

    def __str__(self):
        return self.name


class Department(BaseModel, BaseModel2):
    pass

    def __str__(self):
        return self.name


class Year(BaseModel, BaseModel2):
    pass

    def __str__(self):
        return self.name


class Section(BaseModel, BaseModel2):
    pass

    def __str__(self):
        return self.name


class Semester(BaseModel, BaseModel2):
    pass

    def __str__(self):
        return self.name


class Batch(BaseModel):
    start_year = models.IntegerField(null=False)
    end_year = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.start_year}-{self.end_year}'


class Regulation(BaseModel):
    year = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.year}'


class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_user', null=True, blank=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    register_id = models.BigIntegerField(null=False)
    email = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='stu_dept')
    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name='stu_year')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='sec')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='student_sem')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='stu_batch')
    regulation = models.ForeignKey(Regulation, on_delete=models.CASCADE, related_name='stu_regulation')
    Active = models.BooleanField(default=False)
    Staff_status = models.BooleanField(default=False)
    Superuser_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Subject(BaseModel):
    name = models.CharField(max_length=20)
    sub_code = models.CharField(max_length=10)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='dept_subject')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='sem')
    Regulation = models.ForeignKey(Regulation, on_delete=models.CASCADE, related_name='sub_regulation')

    def __str__(self):
        return self.name


class Staff(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_user')
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=True)
    employee_id = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    mobile_num = models.CharField(max_length=10, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='staff_role')
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='staff_dept', null=True)
    subject = models.ManyToManyField(Subject, blank=True)
    Active = models.BooleanField(default=True)
    Staff_status = models.BooleanField(default=True)
    Superuser_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Marks(BaseModel):
    mark = models.FloatField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students_mark')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f'{self.student}'

