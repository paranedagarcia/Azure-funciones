'''
Carga archivos csv desde un servidor de FTP y sube esos archivos hacia el storage de Azure
dentro de un container 'contenedor'

Autor: Patricio Araneda
Fecha: 2023-08-28
'''
from ftplib import FTP
import os
from pathlib import Path
import logging
from .conexion import conn_FTP
from azure.storage.blob import BlobClient

connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]


def csv_ftp():
    connFTP = conn_FTP()
    Host = str(connFTP[0])
    Puerto = int(connFTP[1])
    Cuenta = str(connFTP[2])
    Pass = str(connFTP[3])

    ftp = FTP()
    ftp.connect(Host, Puerto, timeout=1000)
    ftp.login(user=Cuenta, passwd=Pass)

    files = ['archivo1.csv',
             'archivo1.csv',
             'archivo3.csv']

    logging.info('Se inicia descarga desde FTP Cubit')

    for j in range(len(files)):
        filename = files[j]
        filenameDestino = filename
        try:
            local_filename = os.path.join(r"/tmp/", filenameDestino)
            lf = open(local_filename, "wb")
            ftp.retrbinary("RETR " + filenameDestino, lf.write)
            lf.close()

            blob = BlobClient.from_connection_string(
                conn_str=connect_str, container_name='contenedor', blob_name=filenameDestino)
            with open(file=local_filename, mode="rb") as file:
                blob.upload_blob(file, overwrite=True)
        except ValueError:
            logging.info("Error " + ValueError)


if __name__ == "__main__":
    csv_ftp()
