# Generated by Django 4.1.5 on 2023-01-05 02:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="componentdump",
            name="body",
            field=tinymce.models.HTMLField(),
        ),
    ]