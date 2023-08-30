import os
from celery import Celery
import requests
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_api.settings')
import django
django.setup()
from loan.models import LoanRequest

app = Celery('loan_tasks', broker=os.environ.get('BROKER'))

@app.task
def request_loan_approval(name, document, request_id):
    url = 'https://loan-processor.digitalsys.com.br/api/v1/loan/'
    payload = json.dumps({'name': name, 'document': document})
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        response_data = response.json()
        status = 2
        if response_data['approved']:
            status = 4
        LoanRequest.objects.filter(id=request_id).update(status=status)