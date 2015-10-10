# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'No Data')], null=True)),
                ('occupation', models.IntegerField(default=0)),
                ('zipcode', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('stars', models.PositiveIntegerField()),
                ('citizen', models.ForeignKey(to='movieapp.Rater')),
                ('movie', models.ForeignKey(to='movieapp.Movie')),
            ],
            options={
                'verbose_name_plural': 'ratings',
            },
        ),
    ]
