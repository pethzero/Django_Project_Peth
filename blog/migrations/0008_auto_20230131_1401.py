# Generated by Django 2.1.15 on 2023-01-31 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20230131_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iduser',
            old_name='iduser',
            new_name='userid',
        ),
    ]
