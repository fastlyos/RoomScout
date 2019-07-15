# Generated by Django 2.2.3 on 2019-07-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='date_posted',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='house',
            name='kijiji_link',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
