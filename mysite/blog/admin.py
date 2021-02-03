from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')  # fields displayed on admin page.
    list_filter = ('status', 'created', 'publish')  # sidebar, filter posts
    search_fields = ('title', 'body')  # fields that are searchable using search bar
    prepopulated_fields = {'slug': ('title',)}  # populate slug filed automatically by using the title field's contents
    date_hierarchy = 'publish'  # allows viewing posts based on date.
    ordering = ('status', 'publish')  # ordering of post are by these.


from .models import Post