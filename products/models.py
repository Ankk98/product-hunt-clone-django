from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    publishing_date = models.DateTimeField()
    description = models.TextField()
    img = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes = models.IntegerField(default=0)
    url = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100]

    def publishing_date_pretty(self):
        return self.publishing_date.strftime('%b %e %Y')
