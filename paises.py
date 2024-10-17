import tkinter as tk
from random import choice

# Lista de países y capitales
paises_capitales = [
    ["Afganistán", "Kabul"],
    ["Alemania", "Berlín"],
    ["Argentina", "Buenos Aires"],
    ["Australia", "Canberra"],
    ["Brasil", "Brasilia"],
    ["Canadá", "Ottawa"],
    ["Chile", "Santiago"],
    ["China", "Pekín"],
    ["Colombia", "Bogotá"],
    ["Corea del Sur", "Seúl"],
    ["Egipto", "El Cairo"],
    ["España", "Madrid"],
    ["Estados Unidos", "Washington D.C."],
    ["Francia", "París"],
    ["India", "Nueva Delhi"],
    ["Italia", "Roma"],
    ["Japón", "Tokio"],
    ["México", "Ciudad de México"],
    ["Reino Unido", "Londres"],
    ["Rusia", "Moscú"],
    ["Sudáfrica", "Pretoria"],
    ["Turquía", "Ankara"],
    ["Venezuela", "Caracas"],
    ["Angola", "Luanda"],
    ["Arabia Saudita", "Riad"],
    ["Argelia", "Argel"],
    ["Armenia", "Ereván"],
    ["Austria", "Viena"],
    ["Bangladés", "Daca"],
    ["Bélgica", "Bruselas"],
    ["Bolivia", "Sucre"],
    ["Bulgaria", "Sofía"],
    ["Camerún", "Yaundé"],
    ["Costa Rica", "San José"],
    ["Cuba", "La Habana"],
    ["Dinamarca", "Copenhague"],
    ["Ecuador", "Quito"],
    ["Emiratos Árabes Unidos", "Abu Dabi"],
    ["Filipinas", "Manila"],
    ["Finlandia", "Helsinki"],
    ["Grecia", "Atenas"],
    ["Guatemala", "Ciudad de Guatemala"],
    ["Honduras", "Tegucigalpa"],
    ["Hungría", "Budapest"],
    ["Indonesia", "Yakarta"],
    ["Irán", "Teherán"],
    ["Irlanda", "Dublín"],
    ["Israel", "Jerusalén"],
    ["Jordania", "Amán"],
    ["Kazajistán", "Astaná"],
    ["Líbano", "Beirut"],
    ["Marruecos", "Rabat"],
    ["Nueva Zelanda", "Wellington"],
    ["Pakistán", "Islamabad"],
    ["Panamá", "Ciudad de Panamá"],
    ["Paraguay", "Asunción"],
    ["Perú", "Lima"],
    ["Polonia", "Varsovia"],
    ["Portugal", "Lisboa"],
    ["República Checa", "Praga"],
    ["República Dominicana", "Santo Domingo"],
    ["Senegal", "Dakar"],
    ["Suecia", "Estocolmo"],
    ["Suiza", "Berna"],
    ["Tailandia", "Bangkok"],
    ["Uruguay", "Montevideo"],
    ["Vietnam", "Hanói"]
]

# Variables globales
puntos = 0
pais_actual = None

# Función para actualizar el país
def nuevo_pais():
    global pais_actual
    pais_actual = choice(paises_capitales)
    lbl_pais.config(text=f"Capital de {pais_actual[0]}")

# Función para comprobar la respuesta
def comprobar_respuesta():
    global puntos
    capital = entry_respuesta.get().strip().lower()
    if capital == pais_actual[1].lower():
        puntos += 1
        lbl_resultado.config(text="¡Correcto!", fg="green")
    else:
        puntos -= 1
        lbl_resultado.config(text=f"Incorrecto, era {pais_actual[1]}", fg="red")
    
    lbl_puntos.config(text=f"Puntos: {puntos}")
    entry_respuesta.delete(0, tk.END)  # Limpiar el campo de texto
    nuevo_pais()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Países y Capitales")

# Etiqueta del país
lbl_pais = tk.Label(ventana, text="", font=("Arial", 14))
lbl_pais.pack(pady=10)

# Entrada de texto para la respuesta
entry_respuesta = tk.Entry(ventana, font=("Arial", 14))
entry_respuesta.pack(pady=10)

# Botón para comprobar la respuesta
btn_comprobar = tk.Button(ventana, text="Comprobar", command=comprobar_respuesta, font=("Arial", 12))
btn_comprobar.pack(pady=10)

# Etiqueta para mostrar el resultado
lbl_resultado = tk.Label(ventana, text="", font=("Arial", 14))
lbl_resultado.pack(pady=10)

# Etiqueta para mostrar los puntos
lbl_puntos = tk.Label(ventana, text=f"Puntos: {puntos}", font=("Arial", 14))
lbl_puntos.pack(pady=10)

# Inicializar con un país
nuevo_pais()

# Iniciar el bucle de la ventana
ventana.mainloop()
