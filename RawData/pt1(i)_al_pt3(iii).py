import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import pingouin as pg
from lets_plot import *

LetsPlot.setup_html(no_js=True)

df = pd.read_csv('progra_HE/Northern_Hemisphere_means.csv', skiprows=1, na_values=["*******", "***", " ***"])
df.columns = df.columns.str.strip()

# FORZAR A NÚMEROS: Esta línea convierte todas las columnas a valores numéricos. 
# Si encuentra texto en medio de los datos, lo convierte en un dato vacío (NaN).
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# GRÁFICO 1: Un mes específico (Enero) 
plt.figure(figsize=(10, 5))
plt.plot(df['Year'],
          df['Jan'], 
          color='#1C62C7', 
          linewidth=1.5, 
          label='Enero (Jan)')

plt.axhline(y=0, color='#B30909', 
            linestyle='-', 
            linewidth=1.5, 
            label='Promedio de 1951 a 1980')

plt.title('Anomalía de Temperatura Promedio - Enero')
plt.xlabel('Año')
plt.ylabel('Anomalía de temperatura (°C)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show() # Cierra la ventana de este gráfico para ver el siguiente

# GRÁFICO 2: Promedios de cada estación
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], 
         df['DJF'], 
         color= '#0D82FF', 
         label='Invierno (DJF)', 
         linewidth=1.5)

plt.plot(df['Year'], 
         df['MAM'], 
         color= "#12960B", 
         label='Primavera (MAM)', 
         linewidth=1.5)

plt.plot(df['Year'], 
         df['JJA'], 
         color = "#A330EA", 
         label='Verano (JJA)', 
         linewidth=1.5)

plt.plot(df['Year'], 
         df['SON'], 
         color="#F3BA1D", 
         label='Otoño (SON)', 
         linewidth=1.5)

plt.axhline(y=0, 
            color='#B30909', 
            linestyle='-', 
            linewidth=1.5, 
            label='Promedio de 1951 a 1980')

plt.title('Anomalía de Temperatura Promedio por Estaciones')
plt.xlabel('Año')
plt.ylabel('Anomalía de temperatura (°C)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show() # Cierra la ventana de este gráfico y se abre el ultimo

# GRÁFICO 3: Promedio de anomalías anuales (J-D) 
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], 
         df['J-D'], 
         color='#5A1594', 
         linewidth=1.5, 
         label='Anual (J-D)')

plt.axhline(y=0,
            color='#B30909', 
            linestyle='-', 
            linewidth=1.5, 
            label='Promedio de 1951 a 1980')

plt.title('Anomalía de Temperatura Promedio Anual')
plt.xlabel('Año')
plt.ylabel('Anomalía de temperatura (°C)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()