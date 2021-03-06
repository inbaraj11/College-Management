# Generated by Django 3.2.2 on 2021-05-13 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
                ('college_status', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'NAAC'), (2, 'NBA'), (3, 'NONE')], max_length=3)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('year', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('sub_code', models.CharField(max_length=10)),
                ('Regulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_regulation', to='clgeapp.regulation')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept_subject', to='clgeapp.department')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sem', to='clgeapp.semester')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('register_id', models.BigIntegerField()),
                ('email', models.CharField(max_length=50)),
                ('Active', models.BooleanField(default=False)),
                ('Staff_status', models.BooleanField(default=False)),
                ('Superuser_status', models.BooleanField(default=False)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_batch', to='clgeapp.batch')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_dept', to='clgeapp.department')),
                ('regulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_regulation', to='clgeapp.regulation')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sec', to='clgeapp.section')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_sem', to='clgeapp.semester')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stu_year', to='clgeapp.year')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100, null=True)),
                ('employee_id', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('mobile_num', models.CharField(max_length=10, null=True)),
                ('Active', models.BooleanField(default=True)),
                ('Staff_status', models.BooleanField(default=True)),
                ('Superuser_status', models.BooleanField(default=False)),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_dept', to='clgeapp.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_role', to='clgeapp.role')),
                ('subject', models.ManyToManyField(blank=True, to='clgeapp.Subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('mark', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_mark', to='clgeapp.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='clgeapp.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
