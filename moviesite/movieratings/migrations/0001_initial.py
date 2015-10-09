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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'Did not answer')], max_length=1, null=True)),
                ('occupation', models.IntegerField(default=0)),
                ('zipcode', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('stars', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(to='movieratings.Movie')),
                ('user', models.ForeignKey(to='movieratings.Rater')),
            ],
            options={
                'verbose_name_plural': 'ratings',
            },
        ),
    ]
