# Generated by Django 4.2.4 on 2023-08-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='founder_images/')),
                ('bio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Founders',
        ),
    ]