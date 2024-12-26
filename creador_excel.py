# Para instalar Pandas abrimos la terminal (CTRL + Ñ) y 
# llamamos al Python Install Packaging con la instrudción escrita en terminal 
# pip install pandas openpyxl

import pandas as pd

# Dataframe es la información básica con el día de la semana y su temperatura en 
# grados Celsius
# Creamos un diccionario de Python
data = {
    "Días:": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    "Celsius": [15, 12, 5, 3, 18, 2,-2],
}

df = pd.DataFrame(data)

# Guardamos el DataFrame en un archivo Excel

df.to_excel("conversor_temperaturas.xlsx", index=False) # Crea el archivo Excel

# Para crearlo en CSV La instrucción sería
# df.to_csv("df.to_excel("conversor_temperaturas.csv", index=False)

# Lo ejecutamos así en la terminal
# python .\creador_excel.py
