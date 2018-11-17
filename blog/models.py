from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    index = models.CharField(max_length=2)
    title = models.CharField(max_length=150)
    text = models.TextField()
    create_date = models.DateTimeField(
        default = timezone.now
    )

    def __str__(self):
        return self.index
