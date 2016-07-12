from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ("title","slug","published","status",)
	list_filter = ("status","created","published","author",)
	search_fields = ("title","body",)
	prepopulated_fields = {'slug': ('title',),}
	raw_id_fields = ('author',)
	date_hierarchy = "published"
	ordering = ['status','published',]

admin.site.register(Post,PostAdmin)
