# Generated by Django 3.2.2 on 2021-05-13 11:20

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clgeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='college_status',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('naac', 'NAAC'), ('nba', 'NBA'), ('none', 'NONE')], max_length=5),
        ),
    ]
