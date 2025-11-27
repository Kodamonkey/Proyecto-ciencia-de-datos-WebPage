# Proyecto-ciencia-de-datos

## Correlaciones entre Exoplanetas y Estrellas Anfitrionas

Proyecto de Ciencia de Datos que investiga cómo las propiedades de las estrellas influyen en las características de sus exoplanetas, utilizando datos del telescopio espacial Kepler y técnicas avanzadas de análisis de datos y machine learning.

## 📊 Contenido del Proyecto

- **Notebooks de Análisis** (`notebooks/`):
  - `Exoplanet_EDA_Notebook.ipynb`: Análisis Exploratorio de Datos (EDA)
  - `AnalisisML.ipynb`: Modelos de Machine Learning

- **Datos** (`Data/`):
  - Datos del NASA Exoplanet Archive
  - Archivos CSV con parámetros planetarios y estelares

- **Portfolio Web** (`src/`):
  - Sitio web estático construido con Astro y Tailwind CSS
  - Desplegado en GitHub Pages

- **Documentación** (`Legacy/`):
  - Propuesta inicial del proyecto
  - Documentos de referencia

## 🚀 Instalación y Uso

### Requisitos Previos

- Node.js 18+ y npm

### Instalación

```bash
# Instalar dependencias
npm install

# Ejecutar en modo desarrollo
npm run dev

# Construir para producción
npm run build

# Previsualizar build de producción
npm run preview
```

## 📁 Estructura del Proyecto

```
.
├── notebooks/            # Notebooks de análisis
│   ├── Exoplanet_EDA_Notebook.ipynb
│   └── AnalisisML.ipynb
├── src/                  # Código fuente del sitio web
│   ├── layouts/          # Layouts base de Astro
│   └── pages/            # Páginas del sitio web
├── public/               # Archivos estáticos (favicon, imágenes)
├── Data/                 # Datos del proyecto (CSV)
├── Legacy/               # Documentos originales y referencias
│   ├── PropuestaDeProyectoInicial.pdf
│   └── ProyectoEDA.docx
├── .github/              # Configuración de GitHub Actions
│   └── workflows/        # Workflow de despliegue
├── package.json          # Dependencias de Node.js
├── requirements.txt      # Dependencias de Python
└── README.md
```

## 📊 Generar Visualizaciones

Antes de desplegar, genera las visualizaciones para el sitio web:

```bash
python scripts/generar_visualizaciones.py
```

Esto creará las imágenes en `public/images/visualizaciones/`. Ver `GUIA_VISUALIZACIONES.md` para más detalles.

## 🌐 Despliegue en GitHub Pages

El proyecto está configurado para desplegarse automáticamente en GitHub Pages cuando se hace push a la rama `main`.

**Antes de desplegar, actualiza:**

1. En `astro.config.mjs`: Reemplaza `YOUR_USERNAME` con tu usuario de GitHub
2. En `src/layouts/BaseLayout.astro`: Actualiza los enlaces de GitHub
3. En `src/pages/index.astro`: Actualiza los enlaces a los notebooks (ahora en `notebooks/`)
4. **Genera las visualizaciones** ejecutando el script (ver arriba)

Para habilitar GitHub Pages:
1. Ve a Settings > Pages en tu repositorio
2. Selecciona "GitHub Actions" como fuente
3. El workflow se ejecutará automáticamente en cada push

## 📝 Preguntas de Investigación

1. **Distribución de Tamaños según Tipo de Estrella**
2. **Relación Masa-Masa (Estrella-Planeta)**
3. **Frecuencia de Planetas Gigantes en Distintas Estrellas**
4. **Clasificación de Planetas según Contexto Estelar**
5. **Descubrimientos de Planetas por Tipo y Año**

## 🛠️ Tecnologías Utilizadas

- **Análisis:** Python, Pandas, NumPy, scikit-learn
- **Visualización:** Matplotlib, Seaborn
- **Web:** Astro, Tailwind CSS
- **Datos:** NASA Exoplanet Archive

## 📚 Referencias

- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
- [Exoplanet.eu Catalog](https://exoplanet.eu/)

## 👥 Autores

Equipo del proyecto IMT2200 - Data Science

## 📄 Licencia

Este proyecto utiliza datos públicos del NASA Exoplanet Archive.
