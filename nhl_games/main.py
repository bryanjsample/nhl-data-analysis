from models import Season,  Team, Player, Game, Penalty, Goal, SkaterStats, GoalieStats
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from scraping_funcs import scrape_list_of_seasons
from db_funcs import add_season_to_db

# scrape link to each nhl season from 2005-06 to present
def main():
    seasons = scrape_list_of_seasons()
    season_links = seasons[0]
    print(season_links, '\n\n')
    add_season_to_db(seasons[1])
    # scrape link to each team from each season

        # get team season stats and information (MDA : ANA  \ PHX : ARI  \ ATL)
        # navigate to season gamelog

            # scrape games table on team season page for team game stats and game boxscore link

                # scrape period and game stats from game boxscore page

main()