import numpy as np
import pandas as pd

datos = pb.read_csv('clean_students_complete.csv')
datos.head(2)

nombres = datos["gender"].unique()
pay = datos["gender"].value_counts().plot.pie(figsize=(11,6), labels=nombres , autopct="%0.1f %%")

grados = datos["grade"].unique()
pay2 = datos["grade"].value_counts().plot.pie(figsize=(11,6), labels=grados , autopct="%0.1f %%")
aux = pay2.get_figure()
aux.savefig("Ultima_Grafica.png")
