import requests
import numpy  as np
'''cantidad, min, max'''
data = {                                                        # Objeto JSON enviado a random.org para solicitar los numeros aleatorios
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": "5c256795-b0b4-44bb-a418-7323d45a388b",       # API Key generada para un usuario de random.org. Es gratis.
        "n": 150,                                              # Cantidad de numeros solicitados
        "min": 1,                                               # Numero minimo
        "max": 200000,                                              # Numero maximo
        "replacement": True
    },
    "id": 42
}
r = requests.post('https://api.random.org/json-rpc/2/invoke2', json=data)
# print("Codigo de respuesta solicitud HTTP: " + str(r.status_code))
my_JSON = r.json()
my_data = my_JSON["result"]["random"]["data"]
my_data_array = np.asarray(my_data)

data = my_data_array 
print(data)