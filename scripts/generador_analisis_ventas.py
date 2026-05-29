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
# Agrupamos las ventas por producto y sumamos las cantidades vendidas de cada uno
ventas_por_producto = df.groupby('producto')['cantidad_vendida'].sum()

# Identificamos el producto con mayor cantidad vendida
producto_mas_vendido = ventas_por_producto.idxmax()
cantidad_mas_vendida = ventas_por_producto.max()

print(f"Producto más vendido: {producto_mas_vendido}")
print(f"Cantidad total vendida: {cantidad_mas_vendida} unidades")
# Convertimos la columna fecha_venta a formato de fecha para poder extraer el mes
df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])

# Extraemos el mes y el año de cada fecha y creamos una columna nueva
df['mes'] = df['fecha_venta'].dt.to_period('M')

# Agrupamos por mes y sumamos el monto total de ventas de cada mes
ventas_por_mes = df.groupby('mes')['monto_venta'].sum()

print("Ventas por mes:")
print(ventas_por_mes)
# ── 6. GRÁFICO: EVOLUCIÓN MENSUAL DE VENTAS ──────────────────

# Convertimos el índice a texto para que se pueda usar como etiqueta en el gráfico
meses = ventas_por_mes.index.astype(str)
montos = ventas_por_mes.values

# Creamos el gráfico
plt.figure(figsize=(10, 5))
plt.plot(meses, montos, marker='o')

# Títulos y etiquetas
plt.title('Evolución Mensual de Ventas')
plt.xlabel('Mes')
plt.ylabel('Monto total ($)')
plt.xticks(rotation=45)

plt.tight_layout()

# Guardamos el gráfico en la carpeta resultados
plt.savefig('resultados/evolucion_ventas.png')
plt.show()

print("Gráfico guardado en: resultados/evolucion_ventas.png")
