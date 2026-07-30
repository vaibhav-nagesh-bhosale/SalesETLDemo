from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from config import Config

connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username=Config.POSTGRES_USER,
    password=Config.POSTGRES_PASSWORD,
    host=Config.POSTGRES_HOST,
    port=int(Config.POSTGRES_PORT),
    database=Config.POSTGRES_DATABASE,
)

engine = create_engine(connection_url)

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("✅ PostgreSQL connection successful!")
            print(result.fetchone()[0])
    except Exception as ex:
        print("❌ Connection failed")
        print(ex)