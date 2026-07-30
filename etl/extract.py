import pandas as pd
from azure.storage.blob import BlobServiceClient
from config import Config
from io import BytesIO


def read_csv_from_blob(blob_name):
    client = BlobServiceClient.from_connection_string(
        Config.BLOB_CONNECTION_STRING
    )

    blob = client.get_blob_client(
        container=Config.BLOB_CONTAINER,
        blob=blob_name
    )

    data = blob.download_blob().readall()

    df = pd.read_csv(BytesIO(data))

    return df