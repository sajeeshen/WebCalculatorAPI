# Generated by Django 2.2.2 on 2019-08-26 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_auto_20190826_0544'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operations',
            new_name='Operation',
        ),
        migrations.RenameModel(
            old_name='Reports',
            new_name='Report',
        ),
    ]
