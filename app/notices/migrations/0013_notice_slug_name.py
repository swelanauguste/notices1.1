# Generated by Django 4.1.5 on 2023-01-19 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notices", "0012_notice_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="notice",
            name="slug_name",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
