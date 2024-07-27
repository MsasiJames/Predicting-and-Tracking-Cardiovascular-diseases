# Generated by Django 5.0.3 on 2024-07-25 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_patientdata_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patientdata",
            name="prediction",
        ),
        migrations.AddField(
            model_name="patientdata",
            name="not_presence_prediction",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="patientdata",
            name="presence_prediction",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
