from sqlalchemy import text
from database.db import engine

def log_uploaded_file(
        file_name,
        blob_path,
        file_size,
        uploaded_by,
        status):

    with engine.begin() as conn:

        conn.execute(text("""

        INSERT INTO uploaded_files
        (
            file_name,
            blob_path,
            file_size,
            uploaded_by,
            processing_status
        )

        VALUES
        (
            :file_name,
            :blob_path,
            :file_size,
            :uploaded_by,
            :status
        )

        """),

        {

            "file_name": file_name,

            "blob_path": blob_path,

            "file_size": file_size,

            "uploaded_by": uploaded_by,

            "status": status

        })