# Generated by Django 5.0.2 on 2024-08-11 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_stubjects_departmentid_alter_branches_departmentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='departmentId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.department'),
        ),
        migrations.AlterField(
            model_name='stubjects',
            name='departmentId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.department'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='branchId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.branches'),
        ),
    ]