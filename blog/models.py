from django.db import models
from django.contrib.auth.models import User

class StatusChoices(models.TextChoices):
    DRAFT = '0', 'Draft'
    PUBLISHED = '1', 'Published'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=StatusChoices.choices, default=StatusChoices.DRAFT)
