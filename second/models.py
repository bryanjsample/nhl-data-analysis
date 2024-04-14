from sqlalchemy import create_engine, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from datetime import date, time
from typing import List


engine = create_engine('sqlite:///nhlGames.db')

Base = declarative_base()

class Season(Base):

    __tablename__ = 'seasons'

    # columns
    id : Mapped[str] = mapped_column(String(80), primary_key = True)
    stanleyCupChampionId : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = True)
    stanleyCupRunnerUpId : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = True)
    hartTrophyWinnerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = True)
    vezinaTrophyWinnerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = True)
    calderTrophyWinnerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = True)
    norrisTrophyWinnerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = True)
    connSmytheTrophyWinnerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = True)

    # relationships

    games : Mapped[List['Game']] = relationship(back_populates = 'season')

    stanleyCupChampion : Mapped['Team'] = relationship(back_populates = 'stanleyCupChampionships', foreign_keys = [stanleyCupChampionId])
    stanleyCupRunnerUp : Mapped['Team'] = relationship(back_populates = 'stanleyCupRunnerUps', foreign_keys = [stanleyCupRunnerUpId])
    hartTrophyWinner : Mapped['Player'] = relationship(back_populates = 'hartTrophies', foreign_keys = [hartTrophyWinnerId])
    vezinaTrophyWinner : Mapped['Player'] = relationship(back_populates = 'vezinaTrophies', foreign_keys = [vezinaTrophyWinnerId])
    calderTrophyWinner : Mapped['Player'] = relationship(back_populates = 'calderTrophies', foreign_keys = [calderTrophyWinnerId])
    norrisTrophyWinner : Mapped['Player'] = relationship(back_populates = 'norrisTrophies', foreign_keys = [norrisTrophyWinnerId])
    connSmytheTrophyWinner : Mapped['Player'] = relationship(back_populates = 'connSmytheTrophies', foreign_keys = [connSmytheTrophyWinnerId])

class Team(Base):

    __tablename__ = 'teams'

    # columns
    id : Mapped[str] = mapped_column(String(80), primary_key = True)
    location : Mapped[str] = mapped_column(String(80), nullable = False)
    name : Mapped[str] = mapped_column(String(80), nullable = False)
    conference : Mapped[str] = mapped_column(String(80), nullable = True)

    #relationships
    draftPicks : Mapped[List['Player']] = relationship(back_populates = 'draftTeam')
    homeGames : Mapped[List['Game']] = relationship(back_populates = 'homeTeam')
    awayGames : Mapped[List['Game']] = relationship(back_populates = 'awayTeam')
    penalties : Mapped[List['Penalty']] = relationship(back_populates = 'team')
    goals : Mapped[List['Goal']] = relationship(back_populates = 'team')
    skaterStats : Mapped[List['SkaterStats']] = relationship(back_populates = 'team')
    goalieStats : Mapped[List['GoalieStats']] = relationship(back_populates = 'team')
    stanleyCupChampionships: Mapped[List['Season']] = relationship(back_populates = 'stanleyCupChampion')
    stanleyCupRunnerUps: Mapped[List['Season']] = relationship(back_populates = 'stanleyCupRunnerUp')

class Player(Base):

    __tablename__ = 'players'

    # columns
    id : Mapped[str] = mapped_column(String(80), primary_key = True)
    firstName : Mapped[str] = mapped_column(String(80), nullable = False)
    lastName : Mapped[str] = mapped_column(String(80), nullable = False)
    draftSelection : Mapped[str] = mapped_column(String(80), nullable = True)
    draftedBy : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = True)
    amateurTeams : Mapped[str] = mapped_column(String(80), nullable = True)
    position : Mapped[str] = mapped_column(String(80), nullable = True)
    handedness : Mapped[str] = mapped_column(String(80), nullable = True)
    height : Mapped[int] = mapped_column(Integer, nullable = True)
    weight : Mapped[int] = mapped_column(Integer, nullable = True)
    birthdate : Mapped[date] = mapped_column(Date, nullable = True)
    birthLocationPrimary : Mapped[str] = mapped_column(String(80), nullable = True)
    birthLocationSecondary : Mapped[str] = mapped_column(String(80), nullable = True)
    birthCountry: Mapped[str] = mapped_column(String(80), nullable = True)

    # relationships
    draftTeam : Mapped['Team'] = relationship(back_populates = 'draftPicks', foreign_keys = [draftedBy])

    penalties : Mapped[List['Penalty']] = relationship(back_populates = 'player')
    goals : Mapped[List['Goal']] = relationship(back_populates = 'player')
    primAssists : Mapped[List['Goal']] = relationship(back_populates = 'assist1')
    secAssists : Mapped[List['Goal']] = relationship(back_populates = 'assist2')
    skaterStats : Mapped[List['SkaterStats']] = relationship(back_populates = 'player')
    goalieStats : Mapped[List['GoalieStats']] = relationship(back_populates = 'player')
    hartTrophies : Mapped[List['Season']] = relationship(back_populates = 'hartTrophyWinner')
    vezinaTrophies : Mapped[List['Season']] = relationship(back_populates = 'vezinaTrophyWinner')
    calderTrophies : Mapped[List['Season']] = relationship(back_populates = 'calderTrophyWinner')
    norrisTrophies : Mapped[List['Season']] = relationship(back_populates = 'norrisTrophyWinner')
    connSmytheTrophies : Mapped[List['Season']] = relationship(back_populates = 'connSmytheTrophyWinner')

class Game(Base):

    __tablename__ = 'games'

    # columns
    id : Mapped[str] = mapped_column(String, primary_key = True)
    seasonId : Mapped[str] = mapped_column(String(80), ForeignKey('seasons.id', ondelete = "CASCADE"), nullable = False) 
    gameDate : Mapped[date] = mapped_column(Date, nullable = False) 
    homeTeamId : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = False) 
    homeScore : Mapped[int] = mapped_column(Integer, nullable = False)
    awayTeamId : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = False) 
    awayScore : Mapped[int] = mapped_column(Integer, nullable = False)
    duration : Mapped[time] = mapped_column(Time, nullable = True)
    venue : Mapped[str] = mapped_column(String(80), nullable = True)
    attendance : Mapped[int] = mapped_column(Integer, nullable = True)

    # relationships
    season : Mapped['Season'] = relationship(back_populates = 'games', foreign_keys = [seasonId])
    homeTeam : Mapped['Team'] = relationship(back_populates = 'homeGames', foreign_keys = [homeTeamId])
    awayTeam : Mapped['Team'] = relationship(back_populates = 'awayGames', foreign_keys = [awayTeamId])

    penalties : Mapped[List['Penalty']] = relationship(back_populates = 'game')
    goals : Mapped[List['Goal']] = relationship(back_populates = 'game')
    skaterStats : Mapped[List['SkaterStats']] = relationship(back_populates = 'game')
    goalieStats : Mapped[List['GoalieStats']] = relationship(back_populates = 'game')

class Penalty(Base):

    __tablename__ = 'allPenalties'

    # columns
    id : Mapped[int] = mapped_column(Integer, primary_key = True)
    gameId : Mapped[str] = mapped_column(String(80), ForeignKey('games.id', ondelete = "CASCADE"), nullable = False) 
    period : Mapped[int] = mapped_column(Integer, nullable = False) 
    timeElapsedInPeriod : Mapped[time] = mapped_column(Time, nullable = False) 
    playerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = False) 
    teamId : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = False) 
    penaltyType : Mapped[str] = mapped_column(String(80), nullable = False) 
    timeServed : Mapped[time] = mapped_column(Time, nullable = False)

    # relationships
    game : Mapped['Game'] = relationship(back_populates = 'penalties', foreign_keys = [gameId])
    player : Mapped['Player'] = relationship(back_populates = 'penalties', foreign_keys = [playerId])
    team : Mapped['Team'] = relationship(back_populates = 'penalties', foreign_keys = [teamId])

class Goal(Base):

    __tablename__ = 'allGoals'

    # columns
    id : Mapped[int] = mapped_column(Integer, primary_key = True)
    gameId : Mapped[str] = mapped_column(String(80), ForeignKey('games.id', ondelete = "CASCADE"), nullable = False) 
    period : Mapped[int] = mapped_column(Integer, nullable = False) 
    timeElapsedInPeriod : Mapped[time] = mapped_column(Time, nullable = False) 
    playerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = False) 
    teamId : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = False) 
    goalType : Mapped[str] = mapped_column(String(80), nullable = False)
    assist1Id : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = True) 
    assist2Id : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), nullable = True)

    # relationships
    game : Mapped['Game'] = relationship(back_populates = 'goals', foreign_keys = [gameId])
    player : Mapped['Player'] = relationship(back_populates = 'goals', foreign_keys = [playerId])
    team : Mapped['Team'] = relationship(back_populates = 'goals', foreign_keys = [teamId])
    assist1 : Mapped['Player'] = relationship(back_populates = 'primAssists', foreign_keys = [assist1Id])
    assist2 : Mapped['Player'] = relationship(back_populates = 'secAssists', foreign_keys = [assist2Id])



class SkaterStats(Base):

    __tablename__ = 'playerGameStats'

    # columns
    playerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), primary_key = True) 
    gameId : Mapped[str] = mapped_column(String(80), ForeignKey('games.id', ondelete = "CASCADE"), primary_key = True) 
    teamId : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = False) 
    plusMinus : Mapped[int] = mapped_column(Integer, nullable = True)
    shotsOnGoal : Mapped[int] = mapped_column(Integer, nullable = True)
    shifts : Mapped[int] = mapped_column(Integer, nullable = True)
    timeOnIce : Mapped[time] = mapped_column(Time, nullable = True)

    #relationships
    game : Mapped['Game'] = relationship(back_populates = 'skaterStats', foreign_keys = [gameId])
    player : Mapped['Player'] = relationship(back_populates = 'skaterStats', foreign_keys = [playerId])
    team : Mapped['Team'] = relationship(back_populates = 'skaterStats', foreign_keys = [teamId])

class GoalieStats(Base):

    __tablename__ = 'goalieGameStats'

    # columns
    playerId : Mapped[str] = mapped_column(String(80), ForeignKey('players.id', ondelete = "CASCADE"), primary_key = True) 
    gameId : Mapped[str] = mapped_column(String(80), ForeignKey('games.id', ondelete = "CASCADE"), primary_key = True) 
    teamId : Mapped[str] = mapped_column(String(80), ForeignKey('teams.id', ondelete = "CASCADE"), nullable = False)
    result : Mapped[str] = mapped_column(String(80), nullable = True)
    saves : Mapped[int] = mapped_column(Integer, nullable = True)
    timeOnIce : Mapped[time] = mapped_column(Time, nullable = True)

    # relationships
    game : Mapped['Game'] = relationship(back_populates = 'goalieStats', foreign_keys = [gameId])
    player : Mapped['Player'] = relationship(back_populates = 'goalieStats', foreign_keys = [playerId])
    team : Mapped['Team'] = relationship(back_populates = 'goalieStats', foreign_keys = [teamId])


Base.metadata.create_all(engine)