# Generated by Django 5.0.2 on 2024-08-11 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_department_stubjects_departmentid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='DepartmentId',
            new_name='departmentId',
        ),
    ]
