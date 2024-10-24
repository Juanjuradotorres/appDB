import tkinter as tk
from classshowRecord import ShowRecord
from classGetRecord import  GetRecord
if __name__ == "__main__":
    # URL de la API
    url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    # Crear instancia de GetRecord
    get_record = GetRecord(url)

    # Crear la ventana principal
    ventana = tk.Tk()

    # Crear instancia de ShowRecord y pasarle la instancia de GetRecord
    show_record = ShowRecord(ventana, get_record)

    # Ejecutar la aplicación
    ventana.mainloop()