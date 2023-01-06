# Generated by Django 4.1.5 on 2023-01-05 11:41

import accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0005_navlinkitem_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="navlinkitem",
            name="image",
        ),
        migrations.AddField(
            model_name="testimonial",
            name="image",
            field=models.ImageField(
                default="logo-whitebg.jpg",
                upload_to="pages/testimonials",
                validators=[
                    accounts.validators.validate_file_size,
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["png", "jpg"]
                    ),
                ],
            ),
        ),
    ]
