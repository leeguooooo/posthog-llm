# Generated by Django 3.2.19 on 2023-12-04 02:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0369_user_theme_mode"),
    ]

    operations = [
        migrations.AddField(
            model_name="externaldatajob",
            name="workflow_id",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
