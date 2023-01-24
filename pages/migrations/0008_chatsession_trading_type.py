# Generated by Django 4.1.5 on 2023-01-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_ourrate_alter_sectionbanner_options_chatsession"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatsession",
            name="trading_type",
            field=models.CharField(
                blank=True,
                choices=[(1, "BTC"), (2, "ETH"), (3, "DODGE")],
                max_length=50,
                null=True,
            ),
        ),
    ]
