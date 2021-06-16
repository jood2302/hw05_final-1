from django.contrib import admin

from .models import Comment, Follow, Group, Post

EMPTY_VALUE_DISPLAY = '-пусто-'


class PostsInstanceInline(admin.TabularInline):
    model = Post


class CommentsInstanceInline(admin.TabularInline):
    model = Comment


class FollowsInstanceInline(admin.TabularInline):
    model = Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', 'image', 'id')
    search_fields = ('text', 'author', 'group', 'image')
    list_filter = ('pub_date', 'author', 'group', 'image')
    inlines = [CommentsInstanceInline]
    empty_value_display = EMPTY_VALUE_DISPLAY


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title', 'description', 'slug')
    list_filter = ('title',)
    inlines = [PostsInstanceInline]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created', 'author', 'post')
    search_fields = ('text', 'author', 'post')
    list_filter = ('created', 'author')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user', 'author')


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username')
    search_fields = ('user')
    list_filter = ('user',)
    inlines = [FollowsInstanceInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
