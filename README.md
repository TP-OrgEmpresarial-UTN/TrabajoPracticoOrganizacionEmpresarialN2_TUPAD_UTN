# Análisis de Ventas de una Pequeña Empresa

## Descripción del Proyecto

Trabajo Práctico N°2 de la materia Organización Empresarial — Tecnicatura Universitaria en Programación (TUP) — UTN Modalidad a Distancia.

El proyecto consiste en el análisis de un dataset de ventas comerciales simulado, con el objetivo de generar indicadores básicos que permitan interpretar el desempeño de la empresa a lo largo del tiempo. El flujo de trabajo integra control de versiones con Git y GitHub, gestión de tareas con Jira, y ejecución del código en Google Colab.

---

## Integrantes

| Integrante | Rol | Responsabilidad |
|---|---|---|
| Lautaro Gatti | P1 - Líder y Organizador (Hugo) | Creación del repositorio, estructura de carpetas, README y gestión del proyecto |
| Fiorella Gatti | P2 - Desarrollador Técnico (Paco) | Desarrollo del script de análisis estadístico y procesamiento de datos |
| Lautaro Gatti | P3 - Revisor y QA (Luis) | Peer Review, documentación, control de calidad y gestión de Pull Requests |

---

## Escenario Elegido

**Escenario B — Análisis de Ventas de una Pequeña Empresa**

Análisis de un conjunto de datos simulados de ventas comerciales para generar indicadores básicos de desempeño empresarial, incluyendo ventas totales, producto más vendido y evolución de ventas por mes.

---

## Dataset Utilizado

**Archivo:** `datos/dataset_ventas.csv`  
**Origen:** Dataset generado con ayuda de herramienta de IA Claude 
**Descripción:** Registros simulados de ventas comerciales con información de identificador de producto(id), nombre de producto(producto),cantidad vendida (cantidad_vendida), precio(precio), fecha de venta(fecha_ventaproductos).

---

## Estructura del Repositorio

```
TrabajoPracticoOrganizacionEmpresarialN2_TUPAD_UTN/
│
├── datos/
│   └── dataset_ventas.csv
│
├── scripts/
│   └── generador_analisis_ventas.py
│
├── resultados/
│   └── evolucion_ventas.png
│
├── README.md
│
└── .gitignore
```

---

## Indicadores Analizados

- Ventas totales
- Producto más vendido
- Ventas por mes
- Evolución de ventas en el tiempo (gráfico)

---

## Instrucciones para Ejecutar el Script

### Requisitos

- Python 3.x
- pandas
- matplotlib

### Instalación de dependencias

```bash
pip install pandas matplotlib
```

### Ejecución local

```bash
python scripts/generador_analisis_ventas.py
```

### Ejecución en Google Colab

```python
# 1. Clonar el repositorio
!git clone https://github.com/TP-OrgEmpresarial-UTN/TrabajoPracticoOrganizacionEmpresarialN2_TUPAD_UTN.git
%cd TrabajoPracticoOrganizacionEmpresarialN2_TUPAD_UTN

# 2. Instalar dependencias
!pip install pandas matplotlib

# 3. Ejecutar el script
!python scripts/generador_analisis_ventas.py
```

Los resultados y gráficos generados se guardan automáticamente en la carpeta `/resultados`.

---

## Trazabilidad

Todos los commits siguen el formato de Conventional Commits con referencia al Issue de Jira correspondiente:

```
PROY-1: Crear repositorio en github y definir su estructura
PROY-2: Desarrollar script de análisis de datos
PROY-3: Revisión y documentación del script
```

---

## Institución

**Universidad Tecnológica Nacional (UTN)**  
Tecnicatura Universitaria en Programación — Modalidad a Distancia  
Materia: Organización Empresarial  
Año Lectivo: 2026
