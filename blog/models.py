from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(null=True)
    content = models.TextField()
    postimg = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Comment by {self.name}"
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.email
    


