# Generated by Django 2.2.4 on 2019-08-28 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone_number_confirmed',
            new_name='phone_number_verified',
        ),
    ]
