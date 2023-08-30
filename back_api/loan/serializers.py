from loan.models import LoanRequest, LoanRequestField, LoanRequestValue
from rest_framework import serializers


class LoanRequestFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequestField
        fields = '__all__'

class LoanRequestValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanRequestValue
        exclude = ['loan_request']

class LoanRequestSerializer(serializers.ModelSerializer):
    extra_fields = LoanRequestValueSerializer(many=True)
    
    class Meta:
        model = LoanRequest
        exclude = ['id', 'status']
    
    def create(self, validated_data):
        fields_data = validated_data.pop('extra_fields')
        validated_data['status'] = 3
        loan_request = LoanRequest.objects.create(**validated_data)
        for fdata in fields_data:
            LoanRequestValue.objects.create(loan_request=loan_request, **fdata)
        return loan_request