# Generated by Django 3.1.7 on 2021-02-24 12:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actor', '0001_initial'),
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('year', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2500), django.core.validators.MinValueValidator(1800)])),
                ('image', models.ImageField(blank=True, upload_to='../movie/%Y/%m/%d/')),
                ('rating', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('actors', models.ManyToManyField(blank=True, to='actor.Actor')),
                ('directors', models.ManyToManyField(blank=True, to='director.Director')),
                ('gender', models.ManyToManyField(blank=True, to='movie.Gender')),
            ],
        ),
    ]
