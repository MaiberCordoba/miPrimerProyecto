from django.db import models

# Create your models here.

class Post(models.Model):
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle
