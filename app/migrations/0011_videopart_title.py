# Generated by Django 4.2.4 on 2023-08-21 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_videopart_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='videopart',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
