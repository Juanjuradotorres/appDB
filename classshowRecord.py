import tkinter as tk


class ShowRecord:
    def __init__(self, root, get_record_instance):
        if get_record_instance is None:
            raise ValueError("La instancia de GetRecord no debe ser None")

        self.get_record_instance = get_record_instance

        # Configuración de la ventana
        self.root = root
        self.root.title("Último Registro de Estudiante")
        self.root.geometry("300x200")

        # Crear un botón para obtener el último registro
        self.boton = tk.Button(self.root, text="Mostrar Último Registro", command=self.mostrar_registro)
        self.boton.pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.texto_resultado = tk.Label(self.root, text="", justify=tk.LEFT, font=("Arial", 12))
        self.texto_resultado.pack(pady=10)

    def mostrar_registro(self):
        # Verificar que la instancia de GetRecord exista
        if not hasattr(self.get_record_instance, 'get_latest_record'):
            self.texto_resultado.config(text="Error: No se encontró el método 'get_latest_record'")
            return

        # Obtener el último registro usando la instancia de GetRecord
        resultado = self.get_record_instance.get_latest_record()

        # Si el resultado es un diccionario, se muestran los datos del registro
        if isinstance(resultado, dict):
            id_estudiante = resultado.get('id', 'N/A')
            nombre = resultado.get('nombre', 'N/A')
            apellido = resultado.get('apellido', 'N/A')
            ciudad = resultado.get('ciudad', 'N/A')
            calle = resultado.get('calle', 'N/A')

            # Mostrar el resultado en la etiqueta
            self.texto_resultado.config(
                text=f"ID: {id_estudiante}\nNombre: {nombre}\nApellido: {apellido}\nCiudad: {ciudad}\nCalle: {calle}")
        else:
            # Si el resultado no es un diccionario, mostrar el error o mensaje adecuado
            self.texto_resultado.config(text=f"{resultado}")