# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0003_auto_20151007_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='item_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='stars',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='user_id',
            new_name='user',
        ),
    ]
