# Generated by Django 4.1.5 on 2023-02-07 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_profile_phoneid_profile_phonenumber"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="image",
        ),
    ]