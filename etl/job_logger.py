from sqlalchemy import text
from database.db import engine

def log_job(file_name,
            records,
            status,
            duration,
            error=""):

    with engine.begin() as conn:

        conn.execute(text("""

        INSERT INTO etl_job_history
        (
            file_name,
            source,
            records_loaded,
            status,
            duration_seconds,
            error_message,
            start_time,
            end_time
        )

        VALUES
        (
            :file_name,
            'Azure Blob',
            :records,
            :status,
            :duration,
            :error,
            CURRENT_TIMESTAMP,
            CURRENT_TIMESTAMP
        )

        """),

        {

            "file_name": file_name,

            "records": records,

            "status": status,

            "duration": duration,

            "error": error

        })