from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'author', 'created_at')
    list_filter = ('post_type', 'author')
    search_fields = ('title', 'description', 'content')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    class Media:
        js = ('js/post_admin.js',)