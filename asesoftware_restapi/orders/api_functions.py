from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from orders.utils import extractRequestData, isOrderDataValid, errorMessageRensponse
from orders.models import Order, OrderItem
import json
import requests
import traceback

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProviders(request):
    try:
        providers_list = requests.get("https://raw.githubusercontent.com/Tausandbill/asesoftware-app/refs/heads/main/providers.json").json()
        
        return Response({"data": providers_list})
    except Exception as error:
        traceback.print_exc()
        return Response(errorMessageRensponse("Se ha presentado un error al obtener porveedores:" + str(error)))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createOrder(request):
    try:
        request_data = extractRequestData(request)

        if not request_data:
            Response(errorMessageRensponse("No fue posible extraer los datos de la peticion"))
            
        is_data_valid, error_message = isOrderDataValid(request_data)

        if is_data_valid:
            with transaction.atomic():
                new_order = Order.objects.create(
                    provider_id = request_data['provider_id'],
                    order_date = request_data['order_date']
                )
                
                for item in json.loads(request_data.get("items")):
                    new_order_item = OrderItem.objects.create(
                        order = new_order,
                        product_name = item['name'],
                        quantity = item['quantity'],
                        price = item['price']
                    )

            return Response({"success": 1, "message": "Orden Creada Existosamente"})
        
        else:
            return Response(error_message)
    except Exception as error:
        traceback.print_exc()
        return Response(errorMessageRensponse("Se ha presentado un error al guardar la orden:" + str(error)))