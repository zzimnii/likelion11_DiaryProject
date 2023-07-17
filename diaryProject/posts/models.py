from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=128)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment