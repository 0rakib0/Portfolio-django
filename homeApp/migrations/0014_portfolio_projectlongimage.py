# Generated by Django 4.2.7 on 2023-12-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0013_portfolio_projectdetails_portfolio_projectfeature1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='projectLongImage',
            field=models.ImageField(default=1, upload_to='portfolio-pic'),
            preserve_default=False,
        ),
    ]