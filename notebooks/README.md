# Notebooks de Análisis

Esta carpeta contiene los notebooks de Jupyter utilizados para el análisis del proyecto.

## 📓 Notebooks Disponibles

### `Exoplanet_EDA_Notebook.ipynb`
**Análisis Exploratorio de Datos (EDA)**

Este notebook contiene:
- Carga y limpieza de datos del NASA Exoplanet Archive
- Análisis descriptivo de variables planetarias y estelares
- Visualizaciones exploratorias (histogramas, gráficos de barras, scatter plots)
- Respuestas a las 5 preguntas de investigación desde una perspectiva exploratoria
- Identificación de patrones y tendencias en los datos

**Preguntas abordadas:**
1. Distribución de tamaños según tipo de estrella
2. Relación masa-masa estrella-planeta
3. Frecuencia de planetas gigantes
4. Clasificación de planetas según contexto estelar
5. Descubrimientos de planetas por tipo y año

### `AnalisisML.ipynb`
**Modelos de Machine Learning**

Este notebook contiene:
- Preprocesamiento de datos para machine learning
- Implementación de modelos supervisados:
  - **Clasificación:** SVM, k-NN, Árboles de Decisión, Regresión Logística
  - **Regresión:** KNeighborsRegressor
- Optimización de hiperparámetros con GridSearchCV
- Validación cruzada estratificada (5 folds)
- Evaluación exhaustiva con múltiples métricas
- Comparación de modelos y selección del mejor

**Modelos implementados por pregunta:**
1. **Pregunta 1:** SVC (RBF) - 99% accuracy
2. **Pregunta 2:** KNeighborsRegressor - R² = 0.34
3. **Pregunta 3:** k-NN - 79% accuracy
4. **Pregunta 4:** SVM RBF y k-NN comparados
5. **Pregunta 5:** Múltiples modelos comparados

## 🚀 Cómo Ejecutar

### Requisitos

```bash
pip install -r ../requirements.txt
```

### Ejecutar Notebooks

```bash
# Desde la raíz del proyecto
jupyter notebook notebooks/
```

O abre directamente los archivos `.ipynb` en Jupyter Lab/Notebook.

## 📊 Datos Utilizados

Los notebooks leen datos de la carpeta `../Data/`:
- `PSCompPars_2025.10.17_15.58.36.csv` - Parámetros compuestos del NASA Exoplanet Archive
- `pscomppars.csv` - Versión alternativa
- `datosdaniel.csv` - Dataset adicional
- `exoplaneteu_catalog-1.csv` - Catálogo de Exoplanet.eu

## 📝 Notas

- Los notebooks están diseñados para ejecutarse secuencialmente
- Algunas celdas pueden tardar varios minutos en ejecutarse (especialmente GridSearchCV)
- Los resultados se muestran inline en las celdas de salida
- Se recomienda ejecutar primero el EDA antes del análisis de ML

