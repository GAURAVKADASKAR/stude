# Generated by Django 5.0.2 on 2024-08-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_branches_enddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchId', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('rollNumber', models.CharField(max_length=100)),
                ('branchName', models.CharField(max_length=200)),
            ],
        ),
    ]