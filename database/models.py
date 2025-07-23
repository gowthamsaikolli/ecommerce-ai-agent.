# database/models.py
from sqlalchemy import inspect
from database.connection import engine

def list_tables():
    """Return a list of all tables in the database."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def get_columns(table_name):
    """Return a list of columns for the given table."""
    inspector = inspect(engine)
    return [col["name"] for col in inspector.get_columns(table_name)]

# Example usage for debugging:
if __name__ == "__main__":
    print("Tables:", list_tables())
    for table in list_tables():
        print(f"Columns in {table}:", get_columns(table))



