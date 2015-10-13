# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('favorite_color', models.CharField(max_length=50, blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('web_address', models.URLField(blank=True, null=True)),
                ('twitter_username', models.CharField(validators=[django.core.validators.RegexValidator('@\\w+', message='Twitter names must be composed of alphanumeric characters')], max_length=16, blank=True, null=True)),
                ('following', models.ManyToManyField(to='citizens.Profile', related_name='followers')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
