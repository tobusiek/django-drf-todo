from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    class CategoryName(models.TextChoices):
        NONE = ""
        JOB = "Job"
        HOME = "Home"
        SHOPPING = "Shopping"

    name = models.CharField(
        choices=CategoryName.choices,
        unique=True,
        default=CategoryName.NONE,
        max_length=30,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name or "None"

    class Meta:
        verbose_name_plural = "categories"


class Priority(models.Model):
    class PriorityLevel(models.TextChoices):
        NONE = ""
        LOW = "Low"
        MID = "Medium"
        HIGH = "High"

    level = models.CharField(
        choices=PriorityLevel.choices,
        unique=True,
        default=PriorityLevel.NONE,
        max_length=30,
        blank=True,
    )

    def __str__(self) -> str:
        return self.level or "None"

    class Meta:
        verbose_name_plural = "priorities"


class Progress(models.Model):
    class ProgressLevel(models.TextChoices):
        UNDONE = "Undone"
        IN_PROGRESS = "In progress"
        DONE = "Done"
        WONT_DO = "Won't do"

    status = models.CharField(
        choices=ProgressLevel.choices,
        unique=True,
        default=ProgressLevel.UNDONE,
        max_length=30,
    )

    def __str__(self) -> str:
        return self.status

    class Meta:
        verbose_name_plural = "progress"


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        default=Category.CategoryName.NONE,
        blank=True,
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_DEFAULT,
        default=Priority.PriorityLevel.NONE,
        blank=True,
    )
    progress = models.ForeignKey(
        Progress,
        on_delete=models.PROTECT,
        default=Progress.ProgressLevel.UNDONE,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    due_to = models.DateTimeField(blank=True, null=True)

    def save(self, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(**kwargs)

    def __str__(self) -> str:
        return self.title
