# Generated by Django 4.2.4 on 2023-08-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_pdfbook_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='videopart',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]