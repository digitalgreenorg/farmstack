# Generated by Django 4.1.5 on 2024-02-23 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datahub", "0072_resourcefile_embeddings_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="messages",
            name="prompt_usage",
            field=models.JSONField(default={}, null=True),
        ),
    ]