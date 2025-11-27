"""
Script para generar y guardar visualizaciones clave del análisis de exoplanetas.
Ejecutar desde la raíz del proyecto: python scripts/generar_visualizaciones.py
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo
plt.style.use('dark_background')
sns.set_palette("husl")

# Crear carpeta de salida
output_dir = "public/images/visualizaciones"
os.makedirs(output_dir, exist_ok=True)

# Configurar matplotlib para guardar con fondo transparente
plt.rcParams['figure.facecolor'] = 'none'
plt.rcParams['axes.facecolor'] = '#1a1f3a'
plt.rcParams['savefig.facecolor'] = 'none'
plt.rcParams['savefig.transparent'] = True
plt.rcParams['axes.labelcolor'] = '#e5e7eb'
plt.rcParams['text.color'] = '#e5e7eb'
plt.rcParams['xtick.color'] = '#e5e7eb'
plt.rcParams['ytick.color'] = '#e5e7eb'

print("Generando visualizaciones...")

# ============================================================================
# VISUALIZACIÓN 1: Radio medio por tipo de estrella (Pregunta 1)
# ============================================================================
try:
    ruta = os.path.join("Data", "PSCompPars_2025.10.17_15.58.36.csv")
    archivo = pd.read_csv(ruta, on_bad_lines="skip", skiprows=88)
    
    tipom = archivo[archivo["st_spectype"].str[0] == "M"]
    tipog = archivo[archivo["st_spectype"].str[0] == "G"]
    otros = archivo[(archivo["st_spectype"].str[0] != "G") & (archivo["st_spectype"].str[0] != "M")]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    tipos = ["Tipo M\n(Enanas Rojas)", "Tipo G\n(Similares al Sol)", "Otros Tipos"]
    valores = [tipom["pl_rade"].mean(), tipog["pl_rade"].mean(), otros["pl_rade"].mean()]
    colores = ['#8b5cf6', '#3b82f6', '#60a5fa']
    
    bars = ax.bar(tipos, valores, color=colores, alpha=0.8, edgecolor='white', linewidth=1.5)
    ax.set_ylabel('Radio Medio (R⊕)', fontsize=12, fontweight='bold')
    ax.set_title('Radio Medio de Exoplanetas por Tipo de Estrella', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Agregar valores en las barras
    for bar, val in zip(bars, valores):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{val:.2f}',
                ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "radio_medio_por_tipo_estrella.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Visualización 1: Radio medio por tipo de estrella")
except Exception as e:
    print(f"✗ Error en visualización 1: {e}")

# ============================================================================
# VISUALIZACIÓN 2: Distribución de radios por tipo espectral (Pregunta 1)
# ============================================================================
try:
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].hist(tipom["pl_rade"].dropna(), bins=50, color='#8b5cf6', alpha=0.7, edgecolor='white', linewidth=0.5)
    axes[0].set_title('Tipo M (Enanas Rojas)', fontweight='bold')
    axes[0].set_xlabel('Radio (R⊕)')
    axes[0].set_ylabel('Frecuencia')
    axes[0].grid(alpha=0.3, linestyle='--')
    
    axes[1].hist(tipog["pl_rade"].dropna(), bins=50, color='#3b82f6', alpha=0.7, edgecolor='white', linewidth=0.5)
    axes[1].set_title('Tipo G (Similares al Sol)', fontweight='bold')
    axes[1].set_xlabel('Radio (R⊕)')
    axes[1].set_ylabel('Frecuencia')
    axes[1].grid(alpha=0.3, linestyle='--')
    
    axes[2].hist(otros["pl_rade"].dropna(), bins=50, color='#60a5fa', alpha=0.7, edgecolor='white', linewidth=0.5)
    axes[2].set_title('Otros Tipos', fontweight='bold')
    axes[2].set_xlabel('Radio (R⊕)')
    axes[2].set_ylabel('Frecuencia')
    axes[2].grid(alpha=0.3, linestyle='--')
    
    fig.suptitle('Distribución de Radios Planetarios por Tipo Espectral', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "distribucion_radios_por_tipo.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Visualización 2: Distribución de radios por tipo espectral")
except Exception as e:
    print(f"✗ Error en visualización 2: {e}")

# ============================================================================
# VISUALIZACIÓN 3: Relación masa-masa estrella-planeta (Pregunta 2)
# ============================================================================
try:
    archivo = os.path.join('Data', 'datosdaniel.csv')
    df = pd.read_csv(archivo, on_bad_lines='skip', skiprows=70)
    
    masa = pd.concat([df['pl_bmasse'], df['pl_bmassj'], df['st_mass']], axis=1, ignore_index=False)
    masa_limpia = masa.dropna()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(masa_limpia['pl_bmasse'], masa_limpia['st_mass'], 
                        alpha=0.5, s=20, c=masa_limpia['st_mass'], 
                        cmap='viridis', edgecolors='white', linewidth=0.3)
    ax.set_xlabel('Masa Planetaria (M⊕)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Masa Estelar (M☉)', fontsize=12, fontweight='bold')
    ax.set_title('Relación Masa-Masa: Estrella vs Planeta', fontsize=14, fontweight='bold', pad=20)
    ax.grid(alpha=0.3, linestyle='--')
    plt.colorbar(scatter, ax=ax, label='Masa Estelar (M☉)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "relacion_masa_masa.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Visualización 3: Relación masa-masa")
except Exception as e:
    print(f"✗ Error en visualización 3: {e}")

# ============================================================================
# VISUALIZACIÓN 4: Frecuencia de planetas Júpiter por clase espectral (Pregunta 3)
# ============================================================================
try:
    ruta = os.path.join("Data", "pscomppars.csv")
    df = pd.read_csv(ruta, skiprows=88)
    
    def clase_espectral(s):
        if pd.isna(s) or not isinstance(s, str) or len(s) == 0:
            return np.nan
        return s.strip()[0].upper()
    
    def clasificar_planeta(r_earth):
        if pd.isna(r_earth):
            return np.nan
        r = float(r_earth)
        if r < 1.6:
            return "rocoso"
        elif r < 2.5:
            return "supertierra"
        elif r < 4.0:
            return "neptuno"
        elif r >= 8.0:
            return "jupiter"
        else:
            return "intermedio"
    
    df["spec_class"] = df.get("st_spectype").apply(clase_espectral)
    if "pl_rade" in df.columns:
        df["pl_sizeclass"] = df["pl_rade"].apply(clasificar_planeta)
    
    df_jupiter = df[df["pl_sizeclass"] == "jupiter"]
    jupiter_counts = df_jupiter['spec_class'].value_counts().sort_index()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(range(len(jupiter_counts)), jupiter_counts.values, 
                  color='#f59e0b', alpha=0.8, edgecolor='white', linewidth=1.5)
    ax.set_xticks(range(len(jupiter_counts)))
    ax.set_xticklabels(jupiter_counts.index, rotation=45, ha='right')
    ax.set_xlabel('Clase Espectral', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cantidad de Planetas Tipo Júpiter', fontsize=12, fontweight='bold')
    ax.set_title('Frecuencia de Planetas Tipo Júpiter por Clase Espectral', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Agregar valores
    for bar, val in zip(bars, jupiter_counts.values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(val)}',
                ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "jupiter_por_clase_espectral.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Visualización 4: Frecuencia de planetas Júpiter")
except Exception as e:
    print(f"✗ Error en visualización 4: {e}")

# ============================================================================
# VISUALIZACIÓN 5: Descubrimientos por tipo y año (Pregunta 5)
# ============================================================================
try:
    ruta = os.path.join("Data", "PSCompPars_2025.10.17_15.58.36.csv")
    df_planetas = pd.read_csv(ruta, on_bad_lines="skip", skiprows=88)
    
    otros_tipos = df_planetas[df_planetas["pl_rade"] < 2].copy()
    supertierra = df_planetas[(df_planetas["pl_rade"] >= 2) & (df_planetas["pl_rade"] <= 10)].copy()
    gigantes = df_planetas[df_planetas["pl_rade"] > 10].copy()
    
    otros_tipos["type"] = "Otros"
    supertierra["type"] = "Supertierras"
    gigantes["type"] = "Gigantes"
    
    # Agrupar por año
    otros_anual = otros_tipos.groupby("disc_year").size()
    supertierra_anual = supertierra.groupby("disc_year").size()
    gigantes_anual = gigantes.groupby("disc_year").size()
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    años = sorted(set(list(otros_anual.index) + list(supertierra_anual.index) + list(gigantes_anual.index)))
    
    ax.plot(años, [otros_anual.get(año, 0) for año in años], 
            marker='o', label='Otros', linewidth=2, markersize=6, color='#60a5fa')
    ax.plot(años, [supertierra_anual.get(año, 0) for año in años], 
            marker='s', label='Supertierras', linewidth=2, markersize=6, color='#3b82f6')
    ax.plot(años, [gigantes_anual.get(año, 0) for año in años], 
            marker='^', label='Gigantes Gaseosos', linewidth=2, markersize=6, color='#8b5cf6')
    
    ax.set_xlabel('Año de Descubrimiento', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cantidad de Planetas Descubiertos', fontsize=12, fontweight='bold')
    ax.set_title('Evolución Temporal de Descubrimientos por Tipo de Planeta', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='best', fontsize=11)
    ax.grid(alpha=0.3, linestyle='--')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "descubrimientos_por_tipo_año.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Visualización 5: Descubrimientos por tipo y año")
except Exception as e:
    print(f"✗ Error en visualización 5: {e}")

# ============================================================================
# VISUALIZACIÓN 6: Distribución de composición por tipo espectral (Pregunta 4)
# ============================================================================
try:
    data_path = 'Data/exoplaneteu_catalog-1.csv'
    df = pd.read_csv(data_path, sep=';', low_memory=False)
    
    def clasificar_composicion_simple(fila):
        radio = fila['radius']
        masa = fila['mass']
        if pd.notnull(radio):
            if radio < 0.4:
                return 'Rocoso'
            else:
                return 'Gaseoso'
        elif pd.notnull(masa):
            if masa < 0.15:
                return 'Rocoso'
            else:
                return 'Gaseoso'
        else:
            return 'Desconocido'
    
    def extraer_clase_espectral(tipo_espectral):
        if pd.isna(tipo_espectral) or not isinstance(tipo_espectral, str) or len(tipo_espectral) == 0:
            return np.nan
        return tipo_espectral.strip()[0].upper()
    
    df['composicion'] = df.apply(clasificar_composicion_simple, axis=1)
    df['spec_class'] = df['star_sp_type'].apply(extraer_clase_espectral)
    df_analisis = df[df['composicion'] != 'Desconocido']
    
    distribucion = pd.crosstab(df_analisis['spec_class'], df_analisis['composicion'], normalize='index') * 100
    distribucion = distribucion[['Rocoso', 'Gaseoso']].loc[['M', 'K', 'G', 'F']]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(distribucion.index))
    width = 0.35
    
    bars1 = ax.bar(x - width/2, distribucion['Rocoso'], width, label='Rocoso', 
                   color='#8b5cf6', alpha=0.8, edgecolor='white', linewidth=1)
    bars2 = ax.bar(x + width/2, distribucion['Gaseoso'], width, label='Gaseoso', 
                   color='#3b82f6', alpha=0.8, edgecolor='white', linewidth=1)
    
    ax.set_xlabel('Clase Espectral', fontsize=12, fontweight='bold')
    ax.set_ylabel('Porcentaje (%)', fontsize=12, fontweight='bold')
    ax.set_title('Distribución de Composición Planetaria por Tipo de Estrella', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(distribucion.index)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(0, 100)
    
    # Agregar valores
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "composicion_por_tipo_espectral.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Visualización 6: Distribución de composición")
except Exception as e:
    print(f"✗ Error en visualización 6: {e}")

print(f"\n✅ Visualizaciones guardadas en: {output_dir}/")
print("Las imágenes están listas para usar en el sitio web.")

