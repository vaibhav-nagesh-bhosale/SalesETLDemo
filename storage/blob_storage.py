from azure.storage.blob import BlobServiceClient
from config import Config


class BlobStorage:

    def __init__(self):

        self.client = BlobServiceClient.from_connection_string(
            Config.BLOB_CONNECTION_STRING
        )

        self.container = self.client.get_container_client(
            Config.BLOB_CONTAINER
        )

    def upload_file(self, file):

        blob = self.container.get_blob_client(file.filename)

        blob.upload_blob(
            file.stream,
            overwrite=True
        )

        return file.filename