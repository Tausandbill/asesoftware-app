from datetime import datetime
from orders.errors_dic import errors
import json
import requests
import traceback

def fetchProviders():
    return requests.get("https://raw.githubusercontent.com/Tausandbill/asesoftware-app/refs/heads/main/providers.json").json()

def extractRequestData(request):
    try:
        result = {}
        for key in request.POST:
            result[key] = request.POST.get(key)

        return result
    except Exception as error:
        traceback.print_exc()
        return False


def isOrderDataValid(data):
    try:
        #Validando que se enviara proveedor
        if data.get("provider_id", False) == False:
            return False, errorMessageRensponse('no_provider')
        
        #Validando que se enviara fecha de la orden
        if data.get("order_date", False) == False:
            return False, errorMessageRensponse('no_order_date')
        
        #Validando que se enviaran items
        if data.get("items", False) == False:
            return False, errorMessageRensponse('no_items')   
        
        #Validando un formato valido de fecha
        try:
            datetime.strptime(data.get("order_date"), "%Y-%m-%d")
        except:
            return False, errorMessageRensponse('incorrect_date')

        #Validando un formato valido de items
        try:
            formatted_items = json.loads(data.get("items"))
        except:
            return False, errorMessageRensponse('incorrect_items')
        
        #Validando que el proveedor exista 
        providers_list = fetchProviders()
        provider_exists = any(provider.get("provider_id") == data.get("provider_id") for provider in providers_list)

        if not provider_exists:
            return False, errorMessageRensponse('provider_not_found')
        
        #Validando los items
        for item in formatted_items:
            if not isOrderItemValid(item):
                return False, errorMessageRensponse('incorrect_items')

        return True, {}
    except Exception as error:
        return False, errorMessageRensponse(False, "se presento un error validando los datos:" + str(error))

def isOrderItemValid(item):
    try:
        if item.get("name", False) == False or item.get("quantity", False) == False or item.get("price", False) == False:
            return False
        
        if not isinstance(item.get("name"), str):
            return False
        
        if not isinstance(item.get("quantity"), (int, float)):
            return False
        
        if not isinstance(item.get("price"), (int, float)):
            return False

        return True
    
    except Exception as error:
        traceback.print_exc()
        return False

def errorMessageRensponse(error_key='', message= ''):
    if error_key:
        return {"success": 0, "error": errors[error_key]}
    else:
        return {"success": 0, "error": message}
    
