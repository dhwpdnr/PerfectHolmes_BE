# Generated by Django 3.2 on 2023-12-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Facility",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(help_text="시설명", max_length=100)),
                ("address", models.CharField(help_text="주소", max_length=300)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("유치원", "유치원"),
                            ("초등학교", "초등학교"),
                            ("중학교", "중학교"),
                            ("고등학교", "고등학교"),
                        ],
                        help_text="시설 구분",
                        max_length=50,
                        null=True,
                    ),
                ),
                ("lat", models.FloatField(help_text="위도")),
                ("lng", models.FloatField(help_text="경도")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
