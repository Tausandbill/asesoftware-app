from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.utils import extractRequestData

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProviders(request):
    return Response({"message": "hello world"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createOrder(request):
    extractRequestData(request)
    return Response({"message": "hello world"})