from django.contrib import admin
from.models import Post
from .models import Subscriber

# Register your models here.
admin.site.register(Post)



@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'id')   # show email and ID in the admin list
    search_fields = ('email',)       # allow searching by email


