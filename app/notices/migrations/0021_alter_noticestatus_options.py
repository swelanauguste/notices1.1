# Generated by Django 4.1.5 on 2023-01-22 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("notices", "0020_noticestatus_alter_notice_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="noticestatus",
            options={"ordering": ("status",), "verbose_name_plural": "Notice Statuses"},
        ),
    ]
