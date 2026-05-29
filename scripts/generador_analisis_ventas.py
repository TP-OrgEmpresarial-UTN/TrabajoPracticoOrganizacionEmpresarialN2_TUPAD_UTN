# Importamos las librerías necesarias para el análisis
import pandas as pd
import matplotlib.pyplot as plt

# Leemos el dataset desde la carpeta datos
df = pd.read_csv('datos/dataset_ventas.csv')

# Mostramos las primeras filas para verificar que se cargó correctamente
print(df.head())
print(f"\nEl dataset tiene {len(df)} filas y {len(df.columns)} columnas")
# Calculamos el monto total de cada venta multiplicando cantidad por precio
df['monto_venta'] = df['cantidad_vendida'] * df['precio']

# Sumamos todos los montos para obtener el total general de ventas
ventas_totales = df['monto_venta'].sum()

print(f"Ventas totales: ${ventas_totales:,.2f}")
