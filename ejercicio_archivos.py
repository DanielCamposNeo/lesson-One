import pandas as pb
import numpy as np
import csv

datos = pb.read_csv("athlete_events.csv", index_col=0)
medalla = datos[datos["Medal"].notna()]
df = pb.DataFrame(datos)
#Ejercicio2(Paises mas medalleros)
paises_medallas = df[['NOC','Year']
paises_medallas['NOC'].value_counts().head(10)
paises_medallas['NOC'].value_counts().head(10).plot(kind="bar")

#plots vs time
tiempos = df[["Year","Season","Medal","NOC"]]
tiempos.head(2)
df_2 = pb.get_dummies(tiempos[["Medal"]])
df_2.head(2)
resultado = pb.concat([tiempos,df_2], axis=1)
resultado.head(2)
tiempo2 = resultado.groupby(["Year","Medal","Season"]).sum()
tiempo2["Total Medals"] = tiempo2["Medal_Bronze"] + tiempo2["Medal_Gold"] + tiempo2["Medal_Silver"]
tiempo2
tiempo2.plot(figsize=(50,25))
tiempo_12 = tiempo2[:12]
auxiliar = tiempo_12.plot(figsize=(50,25))
fig = auxiliar.get_figure()
fig.savefig("Grafica Medallero.png")
## Grafica pastel
nombres = tiempo2["Total Medals"][:3].unique()
pastel = tiempo2["Total Medals"][:3].plot.pie(figsize=(11,6),labels= nombres,autopct="%0.1f %%")
auxiliarGrafica = pastel
fig = auxiliarGrafica.get_figure()
fig.savefig("Grafica_Pastel")
#Crea y guarda en una grafica da pay del año mas reciente de la base de datos
final = df["Year"] == "2016"
grafica = final["Total Medals"][:3].plot.pie(figsize=(11,6),labels = nombres,autopct="%0.1f %%")

#Ejercicio primero
'''print("Competidor mas veterano en recibir una medalla de oro")
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
datos["NOC"].value_counts().head(10).plot(kind="bar")'''




"""print(datos["Games"].unique().tolist())
print(datos["Sex"].count())
print(datos["Sex"].value_counts())
print(datos[datos["Age"]==10])
print (datos[datos["Sport"] == "Football"])"""
