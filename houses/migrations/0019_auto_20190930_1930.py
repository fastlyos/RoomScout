# Generated by Django 2.2.4 on 2019-09-30 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0018_auto_20190930_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='is_accessible',
        ),
        migrations.RemoveField(
            model_name='house',
            name='open_to_students',
        ),
        migrations.RemoveField(
            model_name='house',
            name='pets_allowed',
        ),
    ]
