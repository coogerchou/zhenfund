# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_transfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='original_txt',
            field=models.TextField(max_length=100000, null=True),
        ),
    ]
