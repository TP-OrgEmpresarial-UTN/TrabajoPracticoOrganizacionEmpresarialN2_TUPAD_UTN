# Importamos las librerías necesarias para el análisis
import pandas as pd
import matplotlib.pyplot as plt

# ── FUNCIONES ─────────────────────────────────────────────────

def cargar_datos(ruta):
    # Cargamos el archivo CSV y calculamos el monto de cada venta
    df = pd.read_csv(ruta)
    df['monto_venta'] = df['cantidad_vendida'] * df['precio']
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
    return df

def calcular_ventas_totales(df):
    # Sumamos todos los montos para obtener el total general de ventas
    ventas_totales = df['monto_venta'].sum()
    print(f"Ventas totales: ${ventas_totales:,.2f}")

def calcular_producto_mas_vendido(df):
    # Agrupamos por producto y buscamos el de mayor cantidad vendida
    ventas_por_producto = df.groupby('producto')['cantidad_vendida'].sum()
    producto_mas_vendido = ventas_por_producto.idxmax()
    cantidad_mas_vendida = ventas_por_producto.max()
    print(f"Producto más vendido: {producto_mas_vendido}")
    print(f"Cantidad total vendida: {cantidad_mas_vendida} unidades")

def calcular_ventas_por_mes(df):
    # Extraemos el mes de cada fecha y agrupamos los montos
    df['mes'] = df['fecha_venta'].dt.to_period('M')
    ventas_por_mes = df.groupby('mes')['monto_venta'].sum()
    print("Ventas por mes:")
    print(ventas_por_mes.to_string())
    return ventas_por_mes

def graficar_evolucion_ventas(ventas_por_mes):
    # Convertimos el índice a texto para usarlo como etiqueta en el gráfico
    meses = ventas_por_mes.index.astype(str)
    montos = ventas_por_mes.values

    plt.figure(figsize=(10, 5))
    plt.plot(meses, montos, marker='o')

    plt.title('Evolución Mensual de Ventas')
    plt.xlabel('Mes')
    plt.ylabel('Monto total ($)')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig('resultados/evolucion_ventas.png')
    plt.show()
    print("Gráfico guardado en: resultados/evolucion_ventas.png")


# ── PROGRAMA PRINCIPAL ────────────────────────────────────────

df = cargar_datos('datos/dataset_ventas.csv')

calcular_ventas_totales(df)
calcular_producto_mas_vendido(df)
ventas_por_mes = calcular_ventas_por_mes(df)
graficar_evolucion_ventas(ventas_por_mes)
