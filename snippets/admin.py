from django.contrib import admin

from snippets.models import Company, Employee, Employer, Snippet, phoneModel,Invitation,Approver,Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_select_related = ( 'user',)
    search_fields = ['login_date'] 
    list_filter = ('user', 'date')
# Register your models here.
admin.site.register(Snippet)
admin.site.register(phoneModel)
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Invitation)
admin.site.register(Approver)
# admin.site.register(Attendance)