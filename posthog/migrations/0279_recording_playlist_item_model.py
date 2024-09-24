# Generated by Django 3.2.16 on 2022-11-17 14:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0278_organization_customer_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="sessionrecordingplaylist",
            name="is_static",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="SessionRecordingPlaylistItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("session_id", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deleted", models.BooleanField(blank=True, null=True)),
                (
                    "playlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="playlist_items",
                        to="posthog.sessionrecordingplaylist",
                    ),
                ),
            ],
            options={
                "unique_together": {("session_id", "playlist_id")},
            },
        ),
    ]
