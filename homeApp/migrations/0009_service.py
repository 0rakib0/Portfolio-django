# Generated by Django 3.2.20 on 2023-08-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0008_education_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=160)),
                ('serviceIcon', models.CharField(max_length=260)),
                ('aboutService', models.TextField()),
            ],
        ),
    ]
