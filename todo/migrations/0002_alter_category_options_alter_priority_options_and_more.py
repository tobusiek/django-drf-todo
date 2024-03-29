# Generated by Django 4.2.10 on 2024-02-29 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
        migrations.AlterModelOptions(
            name="priority",
            options={"verbose_name_plural": "priorities"},
        ),
        migrations.AlterModelOptions(
            name="progress",
            options={"verbose_name_plural": "progress"},
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.IntegerField(
                choices=[(1, ""), (2, "Job"), (3, "Home"), (4, "Shopping")],
                default=1,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="priority",
            name="level",
            field=models.IntegerField(
                choices=[(1, ""), (2, "Low"), (3, "Medium"), (4, "High")],
                default=1,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="progress",
            name="status",
            field=models.IntegerField(
                choices=[(1, ""), (2, "In progress"), (3, "Done"), (4, "Won't do")],
                default=1,
                unique=True,
            ),
        ),
    ]
