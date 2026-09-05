import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# ============================================================
# 0. Configuración de rutas (basadas en la ubicación del script)
# ============================================================
carpeta_script = Path(__file__).resolve().parent   # carpeta donde está este .py (code/)
carpeta_raw = carpeta_script.parent / "RawData"
carpeta_resultados = carpeta_script.parent / "results"
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# ============================================================
# 1. Cargar y limpiar los datos
# ============================================================
df = pd.read_csv(
    carpeta_raw / "Northern_Hemisphere_means.csv",
    skiprows=1,
    na_values=["*******", "***", " ***"]
)
df.columns = df.columns.str.strip()

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['Year'])

print("Rango de años en los datos:", df['Year'].min(), "-", df['Year'].max())

# ============================================================
# 2. GRÁFICO 1: Un mes específico (Enero)
# ============================================================
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Jan'], color='#1C62C7', linewidth=1.5, label='Enero (Jan)')
plt.axhline(y=0, color='#B30909', linestyle='-', linewidth=1.5, label='Promedio de 1951 a 1980')
plt.title('Anomalía de Temperatura Promedio - Enero')
plt.xlabel('Año')
plt.ylabel('Anomalía de temperatura (°C)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig(carpeta_resultados / "grafico_enero.png", dpi=300, bbox_inches='tight')
plt.show()

# ============================================================
# 3. GRÁFICO 2: Promedios de cada estación
# ============================================================
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['DJF'], color='#0D82FF', label='Invierno (DJF)', linewidth=1.5)
plt.plot(df['Year'], df['MAM'], color='#12960B', label='Primavera (MAM)', linewidth=1.5)
plt.plot(df['Year'], df['JJA'], color='#A330EA', label='Verano (JJA)', linewidth=1.5)
plt.plot(df['Year'], df['SON'], color='#F3BA1D', label='Otoño (SON)', linewidth=1.5)
plt.axhline(y=0, color='#B30909', linestyle='-', linewidth=1.5, label='Promedio de 1951 a 1980')
plt.title('Anomalía de Temperatura Promedio por Estaciones')
plt.xlabel('Año')
plt.ylabel('Anomalía de temperatura (°C)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig(carpeta_resultados / "grafico_estaciones.png", dpi=300, bbox_inches='tight')
plt.show()

# ============================================================
# 4. GRÁFICO 3: Promedio de anomalías anuales (J-D)
# ============================================================
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['J-D'], color='#5A1594', linewidth=1.5, label='Anual (J-D)')
plt.axhline(y=0, color='#B30909', linestyle='-', linewidth=1.5, label='Promedio de 1951 a 1980')
plt.title('Anomalía de Temperatura Promedio Anual')
plt.xlabel('Año')
plt.ylabel('Anomalía de temperatura (°C)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig(carpeta_resultados / "grafico_anual.png", dpi=300, bbox_inches='tight')
plt.show()

# ============================================================
# 5. Tablas de frecuencia por periodo (Parte 1.2)
# ============================================================
periodo_1951_1980 = df[(df['Year'] >= 1951) & (df['Year'] <= 1980)]['J-D']
periodo_1981_2010 = df[(df['Year'] >= 1981) & (df['Year'] <= 2010)]['J-D']

print("\nDatos en 1951-1980:", len(periodo_1951_1980))
print("Datos en 1981-2010:", len(periodo_1981_2010))

bins = np.arange(-0.6, 1.0, 0.1)
tabla_1951_1980 = pd.cut(periodo_1951_1980, bins=bins).value_counts().sort_index()
tabla_1981_2010 = pd.cut(periodo_1981_2010, bins=bins).value_counts().sort_index()

print("\nTabla de frecuencias 1951-1980:")
print(tabla_1951_1980)
print("\nTabla de frecuencias 1981-2010:")
print(tabla_1981_2010)

tabla_1951_1980.to_csv(carpeta_resultados / "tabla_frecuencias_1951_1980.csv")
tabla_1981_2010.to_csv(carpeta_resultados / "tabla_frecuencias_1981_2010.csv")

# ============================================================
# 6. Histograma comparando ambos periodos
# ============================================================
plt.figure(figsize=(10, 5))
plt.hist(periodo_1951_1980, bins=bins, alpha=0.6, label='1951-1980', color='#1C62C7')
plt.hist(periodo_1981_2010, bins=bins, alpha=0.6, label='1981-2010', color='#B30909')
plt.axvline(x=0, color='black', linestyle='--', linewidth=1)
plt.title('Distribución de anomalías de temperatura por periodo')
plt.xlabel('Anomalía de temperatura (°C)')
plt.ylabel('Frecuencia')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig(carpeta_resultados / "histograma_periodos.png", dpi=300, bbox_inches='tight')
plt.show()

# ============================================================
# 7. Deciles 3 y 7 del periodo de referencia (1951-1980)
# ============================================================
decil_3 = np.quantile(periodo_1951_1980.dropna(), 0.3)
decil_7 = np.quantile(periodo_1951_1980.dropna(), 0.7)

print(f"Decil 3 (límite de 'frío'): {decil_3:.3f}")
print(f"Decil 7 (límite de 'caliente'): {decil_7:.3f}")

# ============================================================
# 8. % de anomalías "calientes" en 1981-2010
# ============================================================
calientes_1981_2010 = (periodo_1981_2010 > decil_7).sum()
total_1981_2010 = periodo_1981_2010.dropna().shape[0]
porcentaje_calientes = (calientes_1981_2010 / total_1981_2010) * 100

print(f"Anomalías 'calientes' en 1981-2010: {calientes_1981_2010} de {total_1981_2010}")
print(f"Porcentaje: {porcentaje_calientes:.1f}%")

# ==============================================================
# 9. Medias y varianzas por estación
# ==============================================================
periodos = {
    "1921-1950": (1921, 1950),
    "1951-1980": (1951, 1980),
    "1981-2010": (1981, 2010)
}

estaciones = ["DJF", "MAM", "JJA", "SON"]

for nombre_periodo, (inicio, fin) in periodos.items():
    subset = df[(df['Year'] >= inicio) & (df['Year'] <= fin)]
    print(f"\n--- {nombre_periodo} ---")
    for est in estaciones:
        media = subset[est].mean()
        varianza = subset[est].var()
        print(f"{est}: media = {media:.3f}, varianza = {varianza:.4f}")
        
resultados_varianza = []

for nombre_periodo, (inicio, fin) in periodos.items():
    subset = df[(df['Year'] >= inicio) & (df['Year'] <= fin)]
    for est in estaciones:
        resultados_varianza.append({
            "periodo": nombre_periodo,
            "estacion": est,
            "media": subset[est].mean(),
            "varianza": subset[est].var()
        })

tabla_varianzas = pd.DataFrame(resultados_varianza)
tabla_varianzas.to_csv(carpeta_resultados / "tabla_varianzas_estaciones.csv", index=False)
print(tabla_varianzas)
