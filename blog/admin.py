from django.contrib import admin

# Register your models here.

from .models import Post
from .models import PostAdmin

admin.site.register(Post,PostAdmin)
