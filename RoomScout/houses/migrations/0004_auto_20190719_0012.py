# Generated by Django 2.2.3 on 2019-07-19 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_auto_20190716_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='city',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='house',
            name='postal_code',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='house',
            name='prov_state',
            field=models.CharField(default='', max_length=2),
        ),
    ]
