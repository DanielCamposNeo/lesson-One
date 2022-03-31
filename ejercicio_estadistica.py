import pandas as pb
import numpy as np
import csv

datos = pb.read_csv("clean_students_complete.csv", index_col=0)
data = pb.DataFrame(datos)
print(datos)

corr = datos.corr()
corr.style.background_gradient(cmap="coolwarm")

datos.hist(figsize=(12,4))

datos["grade"].plot(kind = "bar")
