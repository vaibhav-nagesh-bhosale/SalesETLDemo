from sqlalchemy import text
from database.db import engine


class DashboardService:

    @staticmethod
    def get_summary():

        with engine.connect() as conn:

            total_orders = conn.execute(
                text("SELECT COUNT(*) FROM sales")
            ).scalar()

            total_revenue = conn.execute(
                text("""
                    SELECT COALESCE(SUM(totalamount),0)
                    FROM sales
                """)
            ).scalar()

            total_jobs = conn.execute(
                text("""
                    SELECT COUNT(*)
                    FROM etl_job_history
                """)
            ).scalar()

            last_upload = conn.execute(
                text("""
                    SELECT MAX(end_time)
                    FROM etl_job_history
                """)
            ).scalar()

            return {

                "total_orders": total_orders,

                "total_revenue": total_revenue,

                "total_jobs": total_jobs,

                "last_upload": last_upload

            }

    @staticmethod
    def get_recent_jobs():

        with engine.connect() as conn:

            rows = conn.execute(text("""

                SELECT
                    job_id,
                    file_name,
                    records_loaded,
                    status,
                    duration_seconds,
                    end_time

                FROM etl_job_history

                ORDER BY job_id DESC

                LIMIT 10

            """))

            return rows.fetchall()

    @staticmethod
    def get_sales():

        with engine.connect() as conn:

            rows = conn.execute(text("""

                SELECT
                    orderid,
                    product,
                    quantity,
                    price,
                    totalamount

                FROM sales

                ORDER BY orderid

            """))

            return rows.fetchall()