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
    if (row['sepal length (cm)'] >= 5.1) and (row['sepal width (cm)'] >= 3.5) and (row['petal length (cm)'] >= 1.3) and (row['petal width (cm)'] <= 0.2):
        return 'Margaritas'
    else:
        return 'No Margarita'

# Aplicar la función a cada fila y crear la nueva columna 'nuevacolumna'
df['nuevacolumna'] = df.apply(nueva_columna, axis=1)

# Mostrar el DataFrame actualizado
print(df.head())

#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)','petal width (cm)', 'target]

# Ruta al archivo CSV de destino
ruta_archivo_csv = "C:/Users/Juanpablo Lamark/OneDrive/Escritorio/USA/Quinto Semestre Vol5/Toma de Decisiones 1/Vane&juanpa/grupo2/quiz2.csv"

# Usa el método to_csv() para guardar el DataFrame como un archivo CSV
df.to_csv(ruta_archivo_csv, index=False)  # El parámetro index=False evita que se guarde el índice del DataFrame

print("DataFrame guardado como archivo CSV en:", ruta_archivo_csv)

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

#El año y el largo del cépalo no tienen una relación, y a pesar de que hay una tendencia negativa, no es significativa