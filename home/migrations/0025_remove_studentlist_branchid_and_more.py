# Generated by Django 5.0.2 on 2024-08-11 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_stubjects_departmentid_studentlist_branchid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentlist',
            name='branchId',
        ),
        migrations.RemoveField(
            model_name='personalprofile',
            name='username',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='registrationforadmin',
            name='user',
        ),
        migrations.DeleteModel(
            name='stubjects',
        ),
        migrations.DeleteModel(
            name='branches',
        ),
        migrations.DeleteModel(
            name='studentlist',
        ),
        migrations.DeleteModel(
            name='personalProfile',
        ),
        migrations.DeleteModel(
            name='registration',
        ),
        migrations.DeleteModel(
            name='registrationforadmin',
        ),
    ]
