# ⚽ Pipeline de Datos de Ligas de Fútbol

Proyecto **end-to-end de Ingeniería de Datos** utilizando **Apache Airflow, Docker y Snowflake**, enfocado en la extracción, transformación y carga (ETL) de datos de posiciones de ligas de fútbol.

---

## 🚀 Stack Tecnológico

- **Apache Airflow 2** (orquestación de workflows)
- **Docker** (entorno reproducible)
- **Astronomer Runtime**
- **Snowflake** (Data Warehouse)
- **Python** (Pandas)
- **SQL**

---

## 🏗️ Arquitectura del Pipeline

1. **Extracción**  
   Obtención de datos de posiciones de ligas de fútbol desde fuentes públicas.

2. **Transformación**  
   Limpieza y transformación de los datos usando Pandas:
   - Normalización de columnas
   - Enriquecimiento con información de equipos
   - Generación de dataset final

3. **Carga**
   - Exportación de datos a CSV
   - Carga del archivo a un **Stage en Snowflake**
   - Inserción de datos en tablas finales mediante SQL

Todo el proceso está orquestado mediante un **DAG de Airflow**.

---

## ▶️ Ejecución Local

### Requisitos
- Docker
- Astro CLI
- Cuenta en Snowflake

### Pasos

1. Clonar el repositorio:

git clone https://github.com/HiIsai/airflow-football-pipeline.git
cd airflow-football-pipeline

2. Crear el archivo de variables de entorno:

cp .env.example .env


3. Iniciar Airflow:

astro dev start --no-cache


4. Acceder a Airflow:

http://localhost:8080