# Generated by Django 3.1.14 on 2021-12-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("circuits", "0003_auto_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="provider",
            name="account",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
