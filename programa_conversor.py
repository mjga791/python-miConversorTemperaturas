import pandas as pd

# Generamos una función para convertir las temperaturas de celsius a Fharenheit
def celsius_a_Fharenheit(celsius):
    return (celsius * 9 / 5) + 32

# Generamos una función para convertir las temperaturas de Fharenheit a celsius
def Fharenheit_a_celsius(Fharenheit):
    return (Fharenheit - 32) * 5 / 9

# Generamos una función para convertir las temperaturas de celsius a Kelvin
def celsius_a_Kelvin(celsius):
    return celsius + 273.15

# Generamos una función para convertir las temperaturas de Kelvin a celsius
def Kelvin_a_celsius(Kelvin):
    return Kelvin - 273.15

# Para leer el archivo excel:
df = pd.read_excel("conversor_temperaturas.xlsx")

# Vamos añadiendo las distintas columnas con las conversiones

# Añade una columna que llamará "Fharenheit" y que será el resultado de aplicar la función celsius_a_Fharenheit a la columna "Celsius"
df["Fharenheit"] = df["Celsius"].apply(celsius_a_Fharenheit)

# Añade una columna que llamará "Kelvin" y que será el resultado de aplicar la función celsius_a_Kelvin a la columna "Celsius"
df["Kelvin"] = df["Celsius"].apply(celsius_a_Kelvin)

# Añade una columna que llamará "Celsius_de_Fharenheit" y que será el resultado de aplicar la función Fharenheit_a_celsius a la columna "Fharenheit"
df["Celsius_de_Fharenheit"] = df["Fharenheit"].apply(Fharenheit_a_celsius)

# Añade una columna que llamará "Celsius_de_Kelvin" y que será el resultado de aplicar la función Kelvin_a_celsius a la columna "Kelvin"
df["Celsius_de_Kelvin"] = df["Kelvin"].apply(Kelvin_a_celsius)

df.to_excel("temperaturas_convertidas.xlsx", index=False)

print(
    "Se ha terminado la conversión entre temperaturas. Este programa ha creado un nuevo archivo llamado 'temperaturas_convertidas.xlsx'"
)
