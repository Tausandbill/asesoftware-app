from datetime import datetime
import json
import traceback

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
        if data.get("provider_id", False) == False:
            return False, errorMessageRensponse("No se envio Identificador del proveedor")
        
        if data.get("order_date", False) == False:
            return False, errorMessageRensponse("No se envio Fecha de la Orden")
        
        if data.get("items", False) == False:
            return False, errorMessageRensponse("No se envio Items")   
        
        try:
            datetime.strptime(data.get("order_date"), "%Y-%m-%d")
        except:
            return False, errorMessageRensponse("Fecha de orden no valida")

        try:
            formatted_items = json.loads(data.get("items"))
        except:
            return False, errorMessageRensponse("Los items no cumplen la estructura requerida")
        
        for item in formatted_items:
            if not isOrderItemValid(item):
                return False, errorMessageRensponse("Los items no cumplen la estructura requerida")

        return True, {}
    except Exception as error:
        return False, errorMessageRensponse("se presento un error validando los datos:" + str(error))

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

def errorMessageRensponse(message):
    return {"success": 0, "error": message}