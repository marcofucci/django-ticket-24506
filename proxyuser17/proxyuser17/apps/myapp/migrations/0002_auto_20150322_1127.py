# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fkusermodel',
            name='user',
            field=models.ForeignKey(to='core.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='onetooneusermodel',
            name='user',
            field=models.OneToOneField(to='core.User'),
            preserve_default=True,
        ),
    ]
