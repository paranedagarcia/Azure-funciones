# Azure-funciones
Funciones Python para trabajar en Azure

## gsheet
Lee una planilla de Google Sheet, cargando sus valores en un dataframe que se carga a una tabla de Azure SQL Server.

Se requiere establecer una API de conexión solo si la planilla no es de lectura pública. En caso contrario lo recomendable es crear un API de servicio y adjuntar el correo resultante a cada planilla a compartir para aumentar la seguridad.

Para la subida de datos se utiliza la librería pd_to_mssql.
