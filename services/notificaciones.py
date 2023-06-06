import requests
from models.model import notificacionesModel

def enviarCorreo(datos: notificacionesModel):
    print('Enviando correo...', datos.asunto, datos.destino, datos.mensaje)
    #response = requests.get('http://127.0.0.1:5000/correo?destino={}&asunto={}&mensaje={}&hash=ABC123'.format(datos.destino, datos.asunto, datos.mensaje))
    #print(response)