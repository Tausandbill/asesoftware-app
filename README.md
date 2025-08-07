# asesoftware-app
APIR REST de prueba tecnica Asesoftware

En la raiz de projecto se encuentra una coleccion de Postman con los endpoint expuesots por esta aplicación

Endpoints:
- api/token/
- api/sap/providers/
- api/orders/


API Endpoint - POST api/token/
Parametros:
- username
- password

Credenciales de Prueba:
- username: adminuser
- passwrod: 1234


API Endpoint - GET api/sap/providers/
- Se debe enviar un Bearer Token que se obtiene utlizando el endpoint api/token/
- Este retorna el listado de proveedores que se encuentran dentro de este mismo repositorio en el archivo providers.json, este archivo tiene 100 proveedores de ejemplo


API Endpoint - POST api/orders/
- Se debe enviar un Bearer Token que se obtiene utlizando el endpoint api/token/
- En el body de la petición se debe enviar 3 parametros
- El endpoint retorna una respuesta json con la siguiente estructura {"success": 1, "message": "Orden Creada Existosamente"} en caso de ejeccion correcta
- El endpoint retorna una respuesta json con la siguiente estructura {"success": 0, "error": "<Mensaje de error>"} en caso de presentar un error

Parametros:
- provider_id
- order_date
- items

Datos de prueba:
- provider_id = 10
- order_date = 2025-08-04
- items = [{"name":"Sofa", "quantity": 2, "price": 300000}, {"name":"Mesa", "quantity": 1, "price": 230000}]
