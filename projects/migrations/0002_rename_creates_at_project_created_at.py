# Generated by Django 4.2.2 on 2023-06-07 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='creates_at',
            new_name='created_at',
        ),
    ]
