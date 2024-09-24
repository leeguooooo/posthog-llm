# Generated by Django 3.0.3 on 2020-02-25 04:07

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ("posthog", "0023_team_opt_out_capture"),
    ]

    operations = [
        migrations.RunSQL(
            "CREATE INDEX CONCURRENTLY idx_distinct_id ON posthog_event(distinct_id);",
            reverse_sql='DROP INDEX "idx_distinct_id";',
            elidable=True,  # This table no longer exists
        ),
    ]
