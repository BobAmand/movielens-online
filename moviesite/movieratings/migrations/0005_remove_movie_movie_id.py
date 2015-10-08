# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0004_auto_20151008_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='movie_id',
        ),
    ]
