from loan.models import LoanRequestField
from rest_framework import viewsets
from loan.serializers import LoanRequestFieldSerializer, LoanRequestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from loan.tasks import request_loan_approval


class LoanRequestFieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LoanRequestField.objects.all()
    serializer_class = LoanRequestFieldSerializer

@api_view(['POST'])
def create_loan_request(request):
    loan_request = LoanRequestSerializer(data=request.data)
    if not loan_request.is_valid():
        return Response(
            loan_request.errors, status=status.HTTP_400_BAD_REQUEST)
    db_loan_request = loan_request.save()
    request_loan_approval.delay(
        db_loan_request.name,
        db_loan_request.document,
        db_loan_request.id,
    )
    return Response({'message': 'pedido realizado'}, status=status.HTTP_200_OK)
    
