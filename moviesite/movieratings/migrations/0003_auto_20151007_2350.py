# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0002_auto_20151007_0332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='IMDB_URL',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='action',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='adventure',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='animation',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='children_s',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='comedy',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='crime',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='documentary',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='drama',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='fantasy',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='film_noir',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='horror',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='musical',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='mystery',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='romance',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='sci_fi',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='thriller',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video_release_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='war',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='western',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='time_stamp',
        ),
        migrations.AddField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1, null=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'Did not answer')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
