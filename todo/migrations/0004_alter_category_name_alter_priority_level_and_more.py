# Generated by Django 4.2.10 on 2024-02-29 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_alter_category_name_alter_priority_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "None"),
                    ("Job", "Job"),
                    ("Home", "Home"),
                    ("Shopping", "Shopping"),
                ],
                default="",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="priority",
            name="level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "None"),
                    ("Low", "Low"),
                    ("Medium", "Mid"),
                    ("High", "High"),
                ],
                default="",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="progress",
            name="status",
            field=models.CharField(
                choices=[
                    ("Undone", "Undone"),
                    ("In progress", "In Progress"),
                    ("Done", "Done"),
                    ("Won't do", "Wont Do"),
                ],
                default="Undone",
                max_length=30,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="progress",
            field=models.ForeignKey(
                blank=True,
                default="Undone",
                on_delete=django.db.models.deletion.PROTECT,
                to="todo.progress",
            ),
        ),
    ]
