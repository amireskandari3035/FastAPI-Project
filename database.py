from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://project_database_8mld_user:rIWT91aM9Ou3buihkN9ClGkzyRcdoF2E@dpg-cv42v7jtq21c73an7j10-a.frankfurt-postgres.render.com/project_database_8mld"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
