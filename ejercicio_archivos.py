import pandas as pb
import numpy as np
import csv

datos = pb.read_csv("athlete_events.csv", index_col=0)
medalla = datos[datos["Medal"].notna()]

print("Competidor mas veterano en recibir una medalla de oro")
print(medalla[medalla["Medal"]=="Gold"].max())
print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("Competidor mas veterano en recibir una medalla de plata")
print(medalla[medalla["Medal"]=="Silver"].max())
print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("Competidor mas veterano en recibir una medalla de bronce")
print(medalla[medalla["Medal"]=="Bronze"].max())
print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("Competidor mas Joven en recibir una medalla de Oro")
print(medalla[medalla["Medal"]=="Gold"].min())
print("--------------------------------------------------------")
print("--------------------------------------------------------")
print("El Competidor con mas medallas")

nombres = datos.groupby(['Name']).size()
cant = max(nombres)
indice= data.loc[data[0]==cant].index
print(nombres[indice])
print(datos[datos["Name"]=="Robert Tait McKenzie"])
csv = nombres[indice].to_csv('Mayor numero de apariciones', header=True, index = True)
print(csv)

datos = df[["NOC","Year"]]
datos.head(10)
datos["NOC"].value_counts().head(10).plot(kind="bar")


"""print(datos["Games"].unique().tolist())
print(datos["Sex"].count())
print(datos["Sex"].value_counts())
print(datos[datos["Age"]==10])
print (datos[datos["Sport"] == "Football"])"""
