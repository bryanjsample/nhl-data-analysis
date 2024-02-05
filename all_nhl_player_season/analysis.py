from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

password = '8ad7fpx2!' # input('Enter Password: )
db_connection = f'mysql+mysqlconnector://root:{password}@localhost:3306/nhlStats'

engine = create_engine(db_connection)

Base = declarative_base()

Base.metadata.create_all(engine)

def Player():
    pass