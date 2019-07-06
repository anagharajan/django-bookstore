# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20190630_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='latitude',
            field=models.FloatField(default='37.773972', max_length=20),
        ),
        migrations.AddField(
            model_name='review',
            name='longitude',
            field=models.FloatField(default='-122.431297', max_length=20),
        ),
    ]
