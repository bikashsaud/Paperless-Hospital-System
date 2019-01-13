from django.db import models

# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100,blank=True)
    phoneno=models.IntegerField(blank=True)
    comment=models.TextField()

    def __str__(self):
        return self.name
