# Generated by Django 3.2.20 on 2023-08-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0007_remove_skill_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(default=1, max_length=260),
            preserve_default=False,
        ),
    ]
