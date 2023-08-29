from django.contrib import admin
from loan.models import LoanRequest, LoanRequestField

admin.site.register([LoanRequest, LoanRequestField])
