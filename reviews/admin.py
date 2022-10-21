from django.contrib import admin
from .models import Review, Comment

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'content', 'movie_name', 'grade', 'created_at', 'updated_at',]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'review', ]

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)