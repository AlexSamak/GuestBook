from django.db import models


class BookBase(models.Model):
    name = models.CharField(max_length=32)
    comment = models.CharField(max_length=512)
    image = models.FileField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id", "-timestamp"]
