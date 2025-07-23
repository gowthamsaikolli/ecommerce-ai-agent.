# database/connection.py
from sqlalchemy import create_engine

# Path to your SQLite database file.
DATABASE_URL = "sqlite:///data/ecommerce.db"

# Create a SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, echo=False)
