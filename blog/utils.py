from django.core.mail import send_mail
from .models import Subscriber

def notify_subscribers(post):
    emails = [s.email for s in Subscriber.objects.all()]
    send_mail(
        subject=f"New Post: {post.title}",
        message=f"Check out our latest post: {post.title}\n\n{post.summary}\n\nRead more: http://127.0.0.1:8000/blog/detail/{post.pk}/",
        from_email="yourgmail@gmail.com",
        recipient_list=emails,
        fail_silently=False,
    )