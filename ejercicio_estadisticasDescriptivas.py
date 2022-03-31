import pandas as pd
import numpy as np

dicci = {
    "Name" : ["Julian","Daniel","Marta"],
    "Años" : ["19","22","32"],
    "salario" : ["20000","60000","30000"],
    "genero" : ["Masculino","Masculino","Femenino"]
}

data = pd.DataFrame(dicci)
data.head()

datos_Categoricos = data.select_dtypes(exclude=[np.number])
print("El archivo contiene {} datos categoricos".format(datos_Categoricos.shape[1]))

data.dtypes
data.describe()

print("La diferencia salarial es de : ", int(data["salario"].max()) - int(data["salario"].min()))


corr = data.corr()
corr.style.background_gradient(cmap="coolwarm")

data["Años"].plot(kind = "bar")


#Un ejemplo de matriz de correlación es la altura y el peso de las personas
