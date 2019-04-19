from django.contrib import admin
from archive.models import Post


class ArchiveAdmin(admin.ModelAdmin):
    class Meta:
        model = Post


admin.site.register(Post, ArchiveAdmin)
