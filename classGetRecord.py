import tkinter as tk
import requests

# Clase para obtener el registro (GetRecord)
class GetRecord:
    def __init__(self, url):
        self.url = url

    def get_latest_record(self):
        try:
            # Obtener los datos de la API
            respuesta = requests.get(self.url)
            respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa
            datos = respuesta.json()

            # Retornar el último registro si existe
            if datos and isinstance(datos, list):
                return datos[-1]  # El último registro en la lista
            else:
                return "No se encontraron registros."
        except requests.exceptions.RequestException as e:
            return f"Error al obtener datos: {e}"