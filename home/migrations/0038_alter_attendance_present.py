# Generated by Django 5.0.2 on 2024-08-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_attendance_branchid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='present',
            field=models.IntegerField(default=0),
        ),
    ]