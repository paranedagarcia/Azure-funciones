import pyodbc
import os

def conn_SQL():
    server = os.environ["sqhost"]
    database = os.environ["sqdb"] 
    username = os.environ["squser"]
    password = os.environ["sqpwd"]
    
    connSQL = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';AUTOCOMMIT=FALSE;UID='+username+';PWD='+ password)
    return connSQL
    
def conn_FTP():
    Host = os.environ["ftp_host"]
    Puerto = os.environ["ftp_port"]
    Cuenta = os.environ["ftp_cuenta"]
    Pass = os.environ["ftppwd"]
    connFTP = [Host, Puerto, Cuenta, Pass]
    return connFTP