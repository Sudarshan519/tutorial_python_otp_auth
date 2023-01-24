from django.contrib import admin

from snippets.models import Company, Employee, Employer, Snippet, phoneModel

# Register your models here.
admin.site.register(Snippet)
admin.site.register(phoneModel)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Employer)