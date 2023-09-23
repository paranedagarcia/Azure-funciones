# Azure-funciones
Funciones Python para trabajar en Azure

## gsheet
Lee una planilla de Google Sheet, cargando sus valores un un dataframe que se sube a una tabla de Azure SQL Server.

Se requiere establecer una API de conexión solo si la planilla no es de lectura pública. Para la subida de datos se utiliza la librería pd_to_mssql.
