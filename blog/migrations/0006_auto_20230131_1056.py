# Generated by Django 2.1.15 on 2023-01-31 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rapper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iduser',
            name='profile',
            field=models.FileField(blank=True, default='', null=True, upload_to='documents/'),
        ),
    ]