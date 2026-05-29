# =============================================================
# Script de análisis de ventas - Escenario B
# Desarrollador: Fiorella Gatti
#
# Estructura esperada del CSV:
#   - id: identificador único de cada venta (numérico)
#   - producto: nombre del producto vendido (texto)
#   - cantidad_vendida: unidades vendidas en esa transacción (numérico)
#   - precio: precio unitario del producto (numérico)
#   - fecha_venta: fecha de la venta en formato YYYY-MM-DD
# =============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os

# ── FUNCIONES ─────────────────────────────────────────────────

def cargar_datos(ruta):
    # Verifica que la carpeta donde está el archivo exista
    carpeta = os.path.dirname(ruta)
    if carpeta and not os.path.exists(carpeta):
        print(f"Error: no se encontró el directorio '{carpeta}'")
        return None

    # Verifica que el archivo CSV exista
    if not os.path.exists(ruta):
        print(f"Error: no se encontró el archivo '{ruta}'")
        return None

    # Carga el archivo y verifica que no esté vacío
    df = pd.read_csv(ruta)
    if df.empty:
        print("Error: el archivo CSV está vacío")
        return None

    # Verifica que el CSV tenga las columnas necesarias para el análisis
    columnas_requeridas = ['producto', 'cantidad_vendida', 'precio', 'fecha_venta']
    columnas_faltantes = [c for c in columnas_requeridas if c not in df.columns]
    if columnas_faltantes:
        print(f"Error: el CSV no tiene las siguientes columnas requeridas: {columnas_faltantes}")
        return None

    # Calcula el monto de cada venta y convierte la fecha a formato de fecha
    df['monto_venta'] = df['cantidad_vendida'] * df['precio']
    df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
    return df

def calcular_ventas_totales(df):
    # Suma todos los montos individuales para obtener el ingreso total del período.
    # El monto de cada fila fue calculado en cargar_datos() como cantidad * precio.
    ventas_totales = df['monto_venta'].sum()
    print(f"Ventas totales: ${ventas_totales:,.2f}")

def calcular_producto_mas_vendido(df):
    # Agrupa todas las filas por nombre de producto y suma las unidades vendidas.
    # Se usa cantidad_vendida (no monto) para reflejar volumen real de movimiento,
    # independientemente del precio de cada producto.
    ventas_por_producto = df.groupby('producto')['cantidad_vendida'].sum()
    producto_mas_vendido = ventas_por_producto.idxmax()
    cantidad_mas_vendida = ventas_por_producto.max()
    print(f"Producto más vendido: {producto_mas_vendido}")
    print(f"Cantidad total vendida: {cantidad_mas_vendida} unidades")

def calcular_ventas_por_mes(df):
    # Extrae el año y mes de cada fecha para agrupar las ventas mensualmente.
    # to_period('M') agrupa por año-mes (ej: 2024-01), lo que evita mezclar
    # el mismo mes de distintos años si el dataset tuviera más de un año de datos.
    df['mes'] = df['fecha_venta'].dt.to_period('M')
    ventas_por_mes = df.groupby('mes')['monto_venta'].sum()
    print("Ventas por mes:")
    for mes, monto in ventas_por_mes.items():
        print(f"  {mes}: ${monto:,.2f}")
    return ventas_por_mes

def graficar_evolucion_ventas(ventas_por_mes):
    # Verifica que la carpeta resultados exista antes de intentar guardar el gráfico.
    # Si no existe, la crea automáticamente.
    os.makedirs('resultados', exist_ok=True)

    # Convierte el índice a texto para usarlo como etiqueta en el eje X
    meses = ventas_por_mes.index.astype(str)
    montos = ventas_por_mes.values

    # Genera un gráfico de línea que muestra la evolución del monto
    # total de ventas a lo largo de los meses del dataset
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

# Si cargar_datos() devolvió None por algún error, se detiene el programa
if df is not None:
    calcular_ventas_totales(df)
    calcular_producto_mas_vendido(df)
    ventas_por_mes = calcular_ventas_por_mes(df)
    graficar_evolucion_ventas(ventas_por_mes)
