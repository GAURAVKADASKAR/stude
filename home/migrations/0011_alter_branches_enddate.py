# Generated by Django 5.0.2 on 2024-08-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_branches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branches',
            name='enddate',
            field=models.DateField(),
        ),
    ]