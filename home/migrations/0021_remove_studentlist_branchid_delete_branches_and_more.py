# Generated by Django 5.0.2 on 2024-08-11 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_rename_departmentid_department_departmentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentlist',
            name='branchId',
        ),
        migrations.DeleteModel(
            name='branches',
        ),
        migrations.DeleteModel(
            name='studentlist',
        ),
    ]