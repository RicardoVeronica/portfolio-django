from django.db import models
from ckeditor.fields import RichTextField


class Project(models.Model):
    """
    data for each project in my portfolio
    """
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField()
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
