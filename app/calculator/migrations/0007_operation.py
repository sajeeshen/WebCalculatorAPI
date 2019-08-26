# Generated by Django 2.2.2 on 2019-08-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_delete_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_name', models.CharField(max_length=100)),
                ('admin_required', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Operation',
            },
        ),
    ]
