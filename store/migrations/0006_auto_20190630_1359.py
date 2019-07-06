# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to=store.models.cover_upload_path, default='books/empty_cover.jpg'),
        ),
    ]
