import requests

ciudad_origen = "-33.4489,-70.6693"  
ciudad_destino = "-34.6037,-58.3816"


api_url = "https://graphhopper.com/api/1/route"

api_key = "4b199d19-59c2-4040-b5e3-641eb988e31f" 

while True:
   
    params = {
        "point": [ciudad_origen, ciudad_destino],  
        "type": "json",  
        "key": api_key,  
    }

  
    response = requests.get(api_url, params=params)

    
    if response.status_code == 200:
        data = response.json()
        distancia_km = data['paths'][0]['distance'] / 1000  
        duracion_segundos = data['paths'][0]['time'] / 1000  
        duracion_minutos = duracion_segundos / 60  

        
        print(f"\nLa distancia entre Santiago, Chile y Buenos Aires, Argentina es de {distancia_km:.2f} km.")
        print(f"El tiempo estimado del viaje es de {duracion_minutos:.2f} minutos.")
    
    else:
        
        print(f"Error en la solicitud. Código de estado: {response.status_code}")
        print("Detalles del error:", response.text)

    
    salida = input("Presiona 's' para salir o cualquier tecla para calcular otra distancia: ")
    if salida.lower() == 's':
        break