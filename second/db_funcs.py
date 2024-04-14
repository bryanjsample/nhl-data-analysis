import models as db

from sqlalchemy.orm import sessionmaker

def add_season_to_db(season_stats):
    Session = sessionmaker(bind = db.engine)
    session = Session()

    for seasonId, stats in season_stats.items():
        season = db.Season(
            id = seasonId,
            stanleyCupChampionId = stats['stanleyCupChampion'],
            stanleyCupRunnerUpId = stats['stanleyCupRunnerUp'],
            hartTrophyWinnerId = stats['hartTrophyWinner'],
            vezinaTrophyWinnerId = stats['vezinaTrophyWinner'],
            calderTrophyWinnerId = stats['calderTrophyWinner'],
            norrisTrophyWinnerId = stats['norrisTrophyWinner'],
            connSmytheTrophyWinnerId = stats['connSmytheTrophyWinner']
        )
        session.add(season)
        session.commit()
        print(f'Added {seasonId} to database.')

