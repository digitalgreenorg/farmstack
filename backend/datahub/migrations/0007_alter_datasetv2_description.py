# Generated by Django 4.0.5 on 2023-01-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0006_alter_datasetv2_geography_alter_datasetv2_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetv2',
            name='description',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
    ]