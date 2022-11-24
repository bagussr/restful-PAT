from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db = create_engine(DB_URI)

Base = declarative_base()

local_session = sessionmaker(autocommit=False, autoflush=False, bind=db)


def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
