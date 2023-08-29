from django.db import models

class LoanRequestField(models.Model):
    TYPES = [
        (1, "Integer"),
        (2, "String"),
        (3, "Datetime"),
        (4, "Float"),
    ]
    name = models.CharField(max_length=40)
    field_type = models.IntegerField(choices=TYPES)

class LoanRequest(models.Model):
    STATUS_CHOICES = [
        (1, "Aprovada"),
        (2, "Negada"),
        (3, "Aguardando avaliação API"),
        (4, "Aguardando avaliação humana"),
    ]
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES)

class LoanRequestValue(models.Model):
    loan_request = models.ForeignKey(LoanRequest, on_delete=models.CASCADE)
    loan_request_field = models.ForeignKey(LoanRequestField, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
