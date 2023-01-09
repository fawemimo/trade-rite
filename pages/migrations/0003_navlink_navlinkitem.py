# Generated by Django 4.1.5 on 2023-01-05 03:25

from django.db import migrations, models
import django.db.models.deletion
import meta.models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_alter_componentdump_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="NavLink",
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
                ("title", models.CharField(max_length=150)),
                ("descriptions", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="NavLinkItem",
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
                ("title", models.CharField(max_length=150)),
                ("url_link", models.CharField(max_length=50)),
                ("descriptions", models.TextField()),
                (
                    "navlink",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pages.navlink"
                    ),
                ),
            ],
            bases=(meta.models.ModelMeta, models.Model),
        ),
    ]