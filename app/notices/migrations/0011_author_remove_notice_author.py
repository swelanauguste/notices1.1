# Generated by Django 4.1.5 on 2023-01-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notices", "0010_alter_notice_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                ("post", models.TextField(blank=True, null=True)),
                ("tel", models.CharField(blank=True, max_length=15, null=True)),
                ("tel1", models.CharField(blank=True, max_length=15, null=True)),
                ("tel2", models.CharField(blank=True, max_length=15, null=True)),
                ("fax", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="notice",
            name="author",
        ),
    ]
