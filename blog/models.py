from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=settings.AUTH_USER_MODEL, verbose_name='Author')
    title = models.CharField(max_length=200, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Created')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Published')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text