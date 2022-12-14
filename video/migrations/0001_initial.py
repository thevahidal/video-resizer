# Generated by Django 4.1.3 on 2022-11-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("file", models.FileField(upload_to="videos")),
                ("file_240", models.FileField(blank=True, upload_to="videos")),
                ("file_360", models.FileField(blank=True, upload_to="videos")),
                ("resizing_started_at", models.DateTimeField(blank=True, null=True)),
                ("resizing_finished_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
