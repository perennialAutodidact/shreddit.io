# Generated by Django 3.0.2 on 2020-02-04 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chord_progressions', '0003_auto_20200125_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chordprogression',
            name='scales',
        ),
    ]
