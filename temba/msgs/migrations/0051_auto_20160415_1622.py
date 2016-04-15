# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0050_auto_20160414_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='call_type',
            field=models.CharField(help_text='The type of call', max_length=16, verbose_name='Call Type', choices=[('unk', 'Unknown Call Type'), ('mt_call', 'Outgoing Call'), ('mt_miss', 'Missed Outgoing Call'), ('mo_call', 'Incoming Call'), ('mo_miss', 'Missed Incoming Call')]),
        ),
    ]
