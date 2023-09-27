import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

print(df.head())
print(df.columns)


def nueva_columna(row):
    if (row['sepal length (cm)'] >= 5.1) and (row['sepal width (cm)'] >= 3.5) and (row['petal length (cm)'] >= 1.3)and (row['petal width (cm)'] <= 0.2):
        return 'Margaritas'
    else:
        return 'No Margarita'

# Aplicar la función a cada fila y crear la nueva columna 'nuevacolumna'
df['nuevacolumna'] = df.apply(nueva_columna, axis=1)

# Mostrar el DataFrame actualizado
print(df.head())

sns.histplot(data=df, x='nuevacolumna', bins=2)  # Puedes ajustar el número de bins según tus preferencias

# Agrega etiquetas y título al gráfico
plt.xlabel('nuevacolumna')
plt.ylabel('Frecuencia')
plt.title('Histograma de la columna "nuevacolumna"')

# Muestra el histograma
plt.show()



#El histograma de frecuencias rápidamente nos muestra que tenemos 20 margaritas
#La moda sería las no margaritas
####################################################################################################

# Configura el estilo de Seaborn (opcional)
sns.set(style="whitegrid")

# Crea una regresión lineal utilizando Seaborn entre 'sepal length (cm)' y 'sepal width (cm)'
sns.regplot(data=df, x='sepal length (cm)', y='sepal width (cm)', scatter_kws={'alpha':0.5})

# Agrega un título al gráfico
plt.title('Regresión Lineal entre Sepal Length y Sepal Width')

# Muestra el gráfico
plt.show()
