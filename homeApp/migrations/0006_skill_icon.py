# Generated by Django 4.2.4 on 2023-08-09 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0005_education_projectexperience_skill_workexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='icon',
            field=models.CharField(default=1, max_length=260),
            preserve_default=False,
        ),
    ]
