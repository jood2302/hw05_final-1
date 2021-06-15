from django.contrib import admin

from .models import Comment, Follow, Group, Post, User

EMPTY_VALUE_DISPLAY = '-пусто-'

class UsersInstanceInline(admin.TabularInline):
    model = User

class GroupsInstanceInline(admin.TabularInline):
    model = Group

class PostsInstanceInline(admin.TabularInline):
    model = Post

class CommentsInstanceInline(admin.TabularInline):
    model = Comment

class FollowssInstanceInline(admin.TabularInline):
    model = Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text', 'author', 'group')
    list_filter = ('pub_date', 'author', 'group')
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
    list_filter = ('created',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user',)
    


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
