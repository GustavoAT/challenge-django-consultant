from django.contrib import admin
from loan.models import LoanRequest, LoanRequestField, LoanRequestValue

class LoanFieldValueInline(admin.TabularInline):
    model = LoanRequestValue


class LoanRequestAdmin(admin.ModelAdmin):
    inlines = [LoanFieldValueInline]
    list_display = ['document', 'name', 'status']

class LoanRequestFieldAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'field_type']
    
admin.site.register(LoanRequest, LoanRequestAdmin)
admin.site.register(LoanRequestField, LoanRequestFieldAdmin)
