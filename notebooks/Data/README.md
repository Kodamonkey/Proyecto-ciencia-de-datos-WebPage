# Datos del Proyecto

Esta carpeta contiene los datasets utilizados en el análisis de exoplanetas y estrellas anfitrionas.

## 📁 Archivos Disponibles

### `PSCompPars_2025.10.17_15.58.36.csv`
**Planetary Systems Composite Parameters** (versión del 17 de octubre de 2025)

Dataset principal del NASA Exoplanet Archive que contiene:
- Parámetros planetarios: masa, radio, período orbital, excentricidad, etc.
- Parámetros estelares: masa, radio, temperatura efectiva, tipo espectral, metalicidad, etc.
- Información de descubrimiento: método, año, instalación
- ~6,000 registros de exoplanetas confirmados

**Fuente:** [NASA Exoplanet Archive - PSCompPars](https://exoplanetarchive.ipac.caltech.edu/docs/pscp_about.html)

### `pscomppars.csv`
Versión alternativa del dataset de parámetros compuestos.

### `datosdaniel.csv`
Dataset adicional utilizado para análisis específicos de relación masa-masa.

### `exoplaneteu_catalog-1.csv`
Catálogo de exoplanetas de Exoplanet.eu, utilizado como fuente complementaria.

**Fuente:** [Exoplanet.eu Catalog](https://exoplanet.eu/)

## 📊 Estructura de Datos

Los datasets principales incluyen columnas como:

**Planetarias:**
- `pl_name`: Nombre del planeta
- `pl_rade`: Radio planetario (en radios terrestres)
- `pl_bmasse`: Masa planetaria (en masas terrestres)
- `pl_orbper`: Período orbital (días)
- `pl_orbsmax`: Semieje mayor (UA)
- `discoverymethod`: Método de descubrimiento

**Estelares:**
- `hostname`: Nombre de la estrella
- `st_spectype`: Tipo espectral
- `st_mass`: Masa estelar (masas solares)
- `st_rad`: Radio estelar (radios solares)
- `st_teff`: Temperatura efectiva (K)
- `st_met`: Metalicidad

## 🔄 Actualización de Datos

Los datos pueden actualizarse desde:
- [NASA Exoplanet Archive - Data](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars)
- [Exoplanet.eu - Data](https://exoplanet.eu/catalog/)

## ⚠️ Notas

- Los archivos CSV son grandes (~3-4 MB cada uno)
- Algunos valores pueden estar faltantes (NaN) - esto es normal
- Los notebooks incluyen código para manejar valores faltantes
- Se recomienda no modificar los archivos originales; trabajar con copias si es necesario

