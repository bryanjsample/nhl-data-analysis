from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

password = '8ad7fpx2!' # input('Enter Password: )
db_connection = f'mysql+mysqlconnector://root:{password}@localhost:3306/nhlGames'
engine = create_engine(db_connection, echo = True)

Base = declarative_base()

class Season(Base):
    __tablename__ = 'seasons'

class Team(Base):
    __tablename__ = 'teams'

class Player(Base):
    __tablename__ = 'players'

class Game(Base):
    __tablename__ = 'game'

class PeriodPenalties(Base):
    __tablename__ = 'periodPenalties'

class PeriodGoals(Base):
    __tablename__ = 'PeriodGoals'

class TeamGameStats(Base):
    __tablename__ = 'teamGameStats'

class PlayerGameStats(Base):
    __tablename__ = 'playerGameStats'

class GoalieGameStats(Base):
    __tablename__ = 'goalieGameStats'

class TeamSeasonStats(Base):
    __tablename__ = 'teamSeasonStats'

class PlayerSeasonStats(Base):
    __tablename__ = 'playerSeasonStats'

class GoalieSeasonStats(Base):
    __tablename__ = 'goalieSeasonStats'

Base.metadata.create_all(engine)