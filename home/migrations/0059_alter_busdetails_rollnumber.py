# Generated by Django 5.1 on 2024-09-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_busdetails_rollnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busdetails',
            name='rollnumber',
            field=models.TextField(null=True),
        ),
    ]
