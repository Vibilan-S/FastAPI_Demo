from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://vibilan:Vibilan%40123@127.0.0.1:5432/my_project"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
