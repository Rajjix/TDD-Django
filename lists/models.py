from django.db import models
from django.urls import reverse

class List(models.Model):
    pass

    def get_absolute_url(self):
        return reverse('lists:view_list', args=[self.id])

class Item(models.Model):
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
    text = models.TextField()
