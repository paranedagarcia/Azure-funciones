'''
Carga de datos desde Google Sheet a Azure SQL Server mediante Google API y la generación de un archivo JSON con las credenciales de acceso a Google.
La planilla se carga un un dataframe de Pandas y luego se envia a la base de datos mediante la función to_sql de la libreria pd_to_mssql.
Autor: Patricio Araneda
fecha: 2023-09-10
'''
import os
import pandas as pd
import pyodbc
from pd_to_mssql import to_sql
# acceso a Google
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'gskey.json'  # archivo JSON con las credenciales de acceso a Google


def load_gsheet(idg, rango, tabla):
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        KEY, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=idg, range=rango).execute()
    values = result.get('values', [])
    df = pd.DataFrame(values)
    df.columns = df.iloc[0]
    df = df[1:]
    # datos de conexion a Azure SQl Server. Estas deben estar en variables de entorno de su configuracion de la funcion.
    server = os.environ["sqhost"]
    database = os.environ["sqdb"]
    username = os.environ["squser"]
    password = os.environ["sqpwd"]

    conn_str = 'DRIVER={SQL Server};SERVER='+server+';DATABASE=' + \
        database+';AUTOCOMMIT=FALSE;UID='+username+';PWD=' + password
    to_sql(df, tabla, conn_str, schema='dbo', index=True, replace=True,
           chunk_size=1000, thread_count=5, ignore_truncation=False, ignore_missing=False)


# definición de planilla por su ID desde Google Sheet que se encuentra entre d/ y /edit
# https://docs.google.com/spreadsheets/d/12ac5ZNZP8dZ6mM_9DmLt7Ui4gqwCcV1gvRqCwewhQ0Y/edit#gid=0
# reemplaza el id de la planilla por el que corresponda
GS_ID = "12ac123458dZ6mM_9DmL12345gqwCcV1gvRqCwewhqwerty"

load_gsheet(GS_ID, 'Roles', 'roles_dev')
