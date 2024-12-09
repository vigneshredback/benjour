from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "My Admin Dashboard"  # Title at the top
admin.site.site_title = "Admin Portal"         # Title for the browser tab
admin.site.index_title = "Welcome to My Admin Dashboard"  # Subtitle on the homepage



admin.site.register(Journal)
admin.site.register(Paper)