import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------------------------
# Ruta al archivo CSV de origen
archivo_origen = "ServientregaInternational.csv"
# Leer los datos desde el archivo CSV y especificar que la primera fila es el encabezado
datos = pd.read_csv(archivo_origen, delimiter=';', header=0)
#------------------------------------------------------------------------------------------------
print(datos.head())
print(datos.columns)
# Obtener información sobre el DataFrame
print(datos.info())
# Resumen estadístico de las columnas numéricas
print(datos.describe())
#-------------------------------------------------------------------------------------------------

# Convertir las columnas de fecha al formato adecuado
datos['Order Date'] = pd.to_datetime(datos['Order Date'], format='%d/%m/%Y')
datos['Ship Date'] = pd.to_datetime(datos['Ship Date'], format='%d/%m/%Y')

# Calcular la diferencia entre Ship Date y Order Date para obtener el LT
datos['Lead Time'] = datos['Ship Date'] - datos['Order Date']

# Mostrar las primeras filas del DataFrame con la nueva columna
print(datos[['Order Date', 'Ship Date', 'Lead Time']].head())


#------------------------------------------------------------------------------------------

# Convertir la columna 'Lead Time' a días
datos['Lead Time (days)'] = datos['Lead Time'].dt.days

# Crear una gráfica de barras del promedio de Lead Time por Región con color condicional
plt.figure(figsize=(12, 6))

# Obtener el color de la barra más grande
max_region = datos.groupby('Region')['Lead Time (days)'].mean().idxmax()
colors = ['red' if region == max_region else 'grey' for region in datos['Region'].unique()]

# Crear el gráfico de barras
sns.barplot(x='Region', y='Lead Time (days)', data=datos, ci=None, palette=colors)

plt.title('Promedio de Lead Time por Región')
plt.ylabel('Promedio de Lead Time (días)')
plt.show()
#---------------------------------------------------------------------------------------------

# Filtrar el DataFrame para incluir solo la región "Central"
datos_central = datos[datos['Region'] == 'Central']

# Obtener el conteo de filas por categoría en la columna 'State'
conteo_por_estado = datos_central['State'].value_counts()

# Calcular el porcentaje acumulado
porcentaje_acumulado = conteo_por_estado.cumsum() / conteo_por_estado.sum() * 100

# Crear el gráfico de Pareto
fig, ax1 = plt.subplots(figsize=(14, 7))

# Barra para el conteo de filas por categoría
ax1.bar(conteo_por_estado.index, conteo_por_estado, color='lightblue', alpha=0.7)

# Eje y izquierdo para el conteo de filas por categoría
ax1.set_xlabel('Estado')
ax1.set_ylabel('Número de Ventas', color='blue')
ax1.tick_params('y', colors='blue')

# Eje y derecho para el porcentaje acumulado
ax2 = ax1.twinx()
ax2.plot(conteo_por_estado.index, porcentaje_acumulado, color='red', marker='o', ms=5)
ax2.set_ylabel('Porcentaje Acumulado', color='red')
ax2.tick_params('y', colors='red')

# Añadir líneas para resaltar el 80% del porcentaje acumulado
ax2.axhline(y=80, color='green', linestyle='--', linewidth=1)
ax2.text(len(conteo_por_estado) + 1, 80, '80%', color='green', va='center')

# Ajustes adicionales
plt.title('Gráfico de Pareto para Ventas por Estado (Región Central)')
plt.xticks(rotation=45, ha='right')
plt.show()
#------------------------------------------------------------------------------
