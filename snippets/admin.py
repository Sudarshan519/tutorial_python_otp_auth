from django.contrib import admin

from snippets.models import Snippet, phoneModel

# Register your models here.
admin.site.register(Snippet)
admin.site.register(phoneModel)