from django.contrib import admin
from .models import Post, Comment, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','post_author','get_tag_names']

    def get_tag_names(self, post):
        return ','.join([tag.name for tag in post.tags.all()])

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
