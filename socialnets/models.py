from django.db import models


class Link(models.Model):
    key = models.SlugField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
