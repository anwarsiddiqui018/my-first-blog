from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone
from MyApp.models import Post


class norm(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Age = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)





    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Name