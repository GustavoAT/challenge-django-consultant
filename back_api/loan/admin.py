from django.contrib import admin
from loan.models import LoanRequest, LoanRequestField, LoanRequestValue

class LoanFieldValueInline(admin.TabularInline):
    model = LoanRequestValue


class LoanRequestAdmin(admin.ModelAdmin):
    inlines = [LoanFieldValueInline]
    
admin.site.register(LoanRequest, LoanRequestAdmin)
admin.site.register(LoanRequestField)
