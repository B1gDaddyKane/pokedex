import pyodbc
import os

from flask import g
from azure.storage.blob import BlobServiceClient


def get_db():
    if 'db' not in g:
        g.db = pyodbc.connect(
            r'Driver={SQL Server Native Client 11.0};'
            r'Server=play-server.database.windows.net;'
            r'Database=pokedex_db;'
            r'Trusted_Connection=no;'
            r'UID=TestAdmin;'
            r'PWD=Cfd59ahg'
        )

    return g.db.cursor()


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def get_blobclient():
    blob_client = BlobServiceClient.from_connection_string(
        'DefaultEndpointsProtocol=https;AccountName=blobbyblobblob;AccountKey=BU8NtdAV272TeSdamqsxPtiF8mN1ReU5qgCZ73AYcJzLEdICXQugeAT66YA7AIQuCRjoBS1Yuncx5f9njqmg0Q==;EndpointSuffix=core.windows.net')
    return blob_client
