# Generated by Django 4.1.5 on 2023-01-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_navlink_navlinkitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                ("position", models.CharField(max_length=255)),
                ("body", models.TextField()),
            ],
        ),
    ]
