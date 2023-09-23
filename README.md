# Azure-funciones
Funciones Python para trabajar en Azure

Las funciones acá presentadas han sido probadas en entorno de producción y modificadas para ser disponibilizadas en este repositorio.

## gsheet
Lee una planilla de Google Sheet, cargando sus valores en un dataframe que se carga a una tabla de Azure SQL Server.

Se requiere establecer una API de conexión solo si la planilla no es de lectura pública. En caso contrario lo recomendable es crear un API de servicio y adjuntar el correo resultante a cada planilla a compartir para aumentar la seguridad.

Para la subida de datos se utiliza la librería pd_to_mssql.

## ftp_csv
Carga archivos de tipo csv desde un servidor de FTP y sube esos archivos hacia el storage de Azure
dentro de un container 'contenedor'.

El servicio 'Storage accounts' asi com su contenedor deben estar creados y activos.