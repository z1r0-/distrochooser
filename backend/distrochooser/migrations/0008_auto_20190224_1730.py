# Generated by Django 2.1.2 on 2019-02-24 16:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0007_auto_20190223_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultdistroselection',
            name='reason',
        ),
        migrations.AddField(
            model_name='selectionreason',
            name='resultSelection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='distrochooser.ResultDistroSelection'),
        ),
        migrations.AlterField(
            model_name='resultdistroselection',
            name='distro',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='distrochooser.Distribution'),
        ),
        migrations.AlterField(
            model_name='resultdistroselection',
            name='session',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='distrochooser.UserSession'),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 24, 17, 30, 16, 966527)),
        ),
    ]