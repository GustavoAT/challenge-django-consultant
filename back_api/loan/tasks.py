import os
from celery import Celery
import requests
import json
from loan.models import LoanRequest


app = Celery('loan_tasks', broker=os.environ.get('BROKER'))

@app.task
def request_loan_approval(name, document, request_id):
    url = 'https://loan-processor.digitalsys.com.br/api/v1/loan/'
    payload = json.dumps({'name': name, 'document': document})
    # headers = {
    #     'Accept': 'application/json',
    #     'Authorization': f'Bearer {self.token}',
    #     'Content-Type': 'application/json'
    # }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        response_data = response.json()
        status = 2
        if response_data['approved']:
            status = 4
        LoanRequest.objects.filter(id=request_id).update(status=status)