# Generated by Django 2.2.2 on 2019-08-28 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0009_reportrecipient_scheduledreport_scheduledreportgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduledreportgroup',
            name='report',
        ),
        migrations.RemoveField(
            model_name='scheduledreportgroup',
            name='scheduled_report',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.DeleteModel(
            name='ReportRecipient',
        ),
        migrations.DeleteModel(
            name='ScheduledReport',
        ),
        migrations.DeleteModel(
            name='ScheduledReportGroup',
        ),
    ]
