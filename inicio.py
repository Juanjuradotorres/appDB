import tkinter as tk
import requests

# URL de la API
url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"


# Función para obtener y mostrar el último registro
def obtener_ultimo_registro():
    try:
        # Obtener los datos de la API
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa
        datos = respuesta.json()

        # Obtener el último registro
        if datos:
            ultimo_registro = datos[-1]  # El último registro en la lista

            # Extraer los campos
            id_estudiante = ultimo_registro['id']
            nombre = ultimo_registro['nombre']
            apellido = ultimo_registro['apellido']
            ciudad = ultimo_registro['ciudad']
            calle = ultimo_registro['calle']

            # Mostrar los datos en la interfaz
            texto_resultado.config(
                text=f"ID: {id_estudiante}\nNombre: {nombre}\nApellido: {apellido}\nCiudad: {ciudad}\nCalle: {calle}")
        else:
            texto_resultado.config(text="No se encontraron registros.")

    except requests.exceptions.RequestException as e:
        texto_resultado.config(text=f"Error al obtener datos: {e}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Último Registro de Estudiante")
ventana.geometry("300x200")

# Crear un botón para obtener el último registro
boton = tk.Button(ventana, text="Mostrar Último Registro", command=obtener_ultimo_registro)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
texto_resultado = tk.Label(ventana, text="", justify=tk.LEFT, font=("Arial", 12))
texto_resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
