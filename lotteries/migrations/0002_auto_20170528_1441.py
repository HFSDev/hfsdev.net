# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-28 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0001_initial'),
        ('lotteries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinningCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('differentiator', models.PositiveSmallIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='states.City')),
            ],
        ),
        migrations.AlterField(
            model_name='lotodraw',
            name='winning_cities',
            field=models.ManyToManyField(to='lotteries.WinningCity'),
        ),
    ]
