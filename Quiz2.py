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
    if (row['sepal length (cm)'] >= 5.1) and (row['sepal width (cm)'] >= 3.5) and (row['petal length (cm)'] >= 1.3):
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