# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qcaadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simresult',
            name='mode',
            field=models.BooleanField(choices=[(True, 'Sweep'), (False, 'Block')]),
        ),
    ]