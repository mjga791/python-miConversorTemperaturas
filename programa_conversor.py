import pandas as pd


def celsius_a_Fharenheit(celsius):
    return (celsius * 9 / 5) + 32

def Fharenheit_a_celsius(Fharenheit):
    return (Fharenheit - 32) * 5 / 9

def celsius_a_Kelvin(celsius):
    return celsius + 273.15

def Kelvin_a_celsius(Kelvin):
    return Kelvin - 273.15

# Leer el archivo excel:
df = pd.read_excel("conversor_temperaturas.xlsx")

# Añadir una columna al DataFrame que sea de pulgadas y se rellene con el calculo de cm / 2.54

df["Fharenheit"] = df["Celsius"].apply(celsius_a_Fharenheit)
df["Kelvin"] = df["Celsius"].apply(celsius_a_Kelvin)
df["Celsius_de_Fharenheit"] = df["Fharenheit"].apply(Fharenheit_a_celsius)
df["Celsius_de_Kelvin"] = df["Kelvin"].apply(Kelvin_a_celsius)

df.to_excel("temperaturas_convertidas.xlsx", index=False)

print(
    "Se ha terminado la conversión entre temperaturas. Este programa ha creado un nuevo archivo llamado 'temperaturas_convertidas.xlsx'"
)
