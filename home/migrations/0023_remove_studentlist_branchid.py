# Generated by Django 5.0.2 on 2024-08-11 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_branches_studentlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentlist',
            name='branchId',
        ),
    ]
