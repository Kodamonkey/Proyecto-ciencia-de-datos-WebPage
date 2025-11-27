# Guía para Generar Visualizaciones

Esta guía explica cómo generar las imágenes de gráficos para el portfolio web.

## Método Automático (Recomendado)

Ejecuta el script Python que genera todas las visualizaciones automáticamente:

```bash
python scripts/generar_visualizaciones.py
```

El script:
- Lee los datos de la carpeta `Data/`
- Genera 6 visualizaciones clave del análisis
- Guarda las imágenes en `public/images/visualizaciones/` con formato PNG de alta calidad (300 DPI)
- Usa un estilo oscuro que combina con el tema del sitio web

## Visualizaciones Generadas

1. **radio_medio_por_tipo_estrella.png** - Gráfico de barras comparando radio medio por tipo espectral
2. **distribucion_radios_por_tipo.png** - Histogramas de distribución de radios para cada tipo
3. **relacion_masa_masa.png** - Scatter plot de relación masa estrella vs masa planeta
4. **jupiter_por_clase_espectral.png** - Frecuencia de planetas tipo Júpiter por clase espectral
5. **descubrimientos_por_tipo_año.png** - Evolución temporal de descubrimientos por tipo
6. **composicion_por_tipo_espectral.png** - Distribución de composición (rocoso/gaseoso) por tipo espectral

## Método Manual

Si prefieres generar los gráficos manualmente desde los notebooks:

1. Abre `notebooks/Exoplanet_EDA_Notebook.ipynb` o `notebooks/AnalisisML.ipynb`
2. Ejecuta las celdas que generan los gráficos
3. Agrega código para guardar cada gráfico:

```python
plt.savefig('../public/images/visualizaciones/nombre_grafico.png', 
            dpi=300, bbox_inches='tight', facecolor='none', transparent=True)
```

4. Asegúrate de usar `transparent=True` para que el fondo sea transparente y combine con el tema oscuro

## Requisitos

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn

Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Notas

- Las imágenes se generan con fondo transparente para combinar con el tema oscuro del sitio
- Resolución: 300 DPI para calidad profesional
- Formato: PNG para mantener calidad y transparencia
- Estilo: Tema oscuro que combina con el diseño del portfolio

