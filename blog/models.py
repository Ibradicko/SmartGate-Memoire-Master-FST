# blog/models.py

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Champ d'image ajouté

    def get_absolute_url(self):
        return reverse("blogs:blog_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
