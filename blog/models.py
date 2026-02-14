from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', 'title']
    
    def __str__(self):
        return self.title
    
    # ----- URLS -----

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])
