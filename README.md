# TT-Proyecto-5

Proyecto 5 del bootcap "Data Analyst" de TripleTen.
Desarrollado por Óscar López.
Link del repositorio en GitHub: https://github.com/OscarLpzLuna/TT-Proyecto-5.git

En este proyecto se hace el despliegue del panel de control de una aplicación web sencilla
en un servicio en la nube: Render.

La aplicación web consiste la muestra de diferentes gráficos correspondientes al análisis
exploratorio de datos realizado sobre un dataset de venta de vehículos('vehicles_us.csv'),
se incluye el análisis realizado en el archivo 'EDA.ipynb' dentro del directorio 'notebooks'.

Se usaron las siguientes librerias de Python para el desarrollo de este proyecto:
    -Streamlit: Para la construcción de la aplicación web
    -Pandas: Para el análisis y manipulación de los dataframes.
    -Plotly Express: Para la creación de gráficos.

Descripción de los archivos:

- 'config.toml', en el directorio '.streamlit' contiene la información necesaria para configurar
el servidor donde se desplegará la aplicación.
- 'app.py' es el scrip en el cual está construida la aplicación web.
- 'requirements.txt' es un archivo necesario para indicar a Render las librerias necesarias para
correr el script 'app.py'.
- 'vehicles_us.csv', conjunto de datos de interés.



