from database.db import engine
from sqlalchemy import text

with engine.connect() as conn:

    print("Current Database:")
    print(conn.execute(text("SELECT current_database();")).fetchone())

    print("Current User:")
    print(conn.execute(text("SELECT current_user;")).fetchone())

    print("Current Schema:")
    print(conn.execute(text("SELECT current_schema();")).fetchone())

    print("Sales Count:")
    print(conn.execute(text("SELECT COUNT(*) FROM sales;")).fetchone())