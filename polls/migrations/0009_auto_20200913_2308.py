# Generated by Django 2.1.5 on 2020-09-14 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200913_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='notMuchVotes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='theSkyeVotes',
        ),
    ]
