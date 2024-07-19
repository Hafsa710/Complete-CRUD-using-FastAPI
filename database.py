from sqlalchemy.orm import declarative_base,sessionmaker

from sqlalchemy import create_engine

engine =create_engine("postgresql+psycopg2://postgres:tefta@127.0.0.1/Person" ,echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)