# Generated by Django 4.0.5 on 2023-04-19 05:39

import datahub.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub', '0033_alter_usagepolicy_user_organization_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasetv2',
            name='geography_new',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='datasetv2file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=datahub.models.DatasetV2File.get_upload_path),
        ),
        migrations.AlterField(
            model_name='datasetv2file',
            name='standardised_file',
            field=models.FileField(blank=True, null=True, upload_to=datahub.models.DatasetV2File.get_upload_path),
        ),
        migrations.AlterField(
            model_name='usagepolicy',
            name='accessibility_time',
            field=models.DateField(default=datetime.date(2023, 5, 17)),
        ),
    ]
