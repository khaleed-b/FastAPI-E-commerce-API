from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(
                       settings.database_url, 
                       connect_args={"sslmode": "require"},
                       pool_pre_ping=True,     # Checks connection health before each use
                       pool_recycle=300,       # Reconnects every 5 minutes to avoid stale connections
                       pool_size=5,            # Keep a small number of persistent connections
                       max_overflow=10  
                      )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
