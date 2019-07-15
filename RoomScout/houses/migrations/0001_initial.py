# Generated by Django 2.2.3 on 2019-07-15 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('prov_state', models.CharField(max_length=40)),
                ('postal_code', models.CharField(max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, upload_to='images/')),
                ('image5', models.ImageField(blank=True, upload_to='images/')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.House')),
            ],
        ),
    ]
