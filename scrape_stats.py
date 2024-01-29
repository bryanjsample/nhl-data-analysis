from bs4 import BeautifulSoup
import requests
from time import sleep
import sort_stats

def find_web_elements(player_url, player_id):
    # delay and request new player webpage
    sleep(4)
    req = requests.get(player_url)
    soup = BeautifulSoup(req.content, 'html.parser')

    # obtain player information
    player_dict = sort_stats.sort_player_info(soup, player_url, player_id)
    position = find_position(player_dict)

    # find the correct table
    try:
        table = soup.find('table', id = 'stats_basic_nhl')
        if table is None:
            table = soup.find('table', id = 'stats_basic_plus_nhl')
        if table is None:
            raise
    except:
        print(f'Something went wrong with {player_url}')
        table = soup.find('table', id = 'stats_basic_nhl')
        if table is None:
            table = soup.find('table', id = 'stats_basic_plus_nhl')
        if table is None:
            raise

    # obtain all stats from all seasons from table
    list_of_all_seasons = scrape_table(table, player_id, position)
    return (player_dict, list_of_all_seasons)

def find_position(player_dict):
    for key, value in player_dict.items():
        stat_list = value
    position_dict = stat_list[3]
    for key, value in position_dict.items():
        position = value
    return position

def scrape_table(table, player_id, position):
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')
    list_of_all_seasons = []
    # iterate through each row, iterating through each colum
    for row in table_rows:
        stat_column_header = row.find('th') # this is the season
        season_id = '"' + stat_column_header.get_text() + '"'
        stat_column_body = row.find_all('td') # these are all stats
        if position != '"G"':
            stats_lists = sort_stats.sort_player_stats(stat_column_body, player_id, season_id)
            list_of_all_seasons.append(stats_lists)
        elif position == None:
            position = "na"
        else:
            stats_lists = sort_stats.sort_goalie_stats(stat_column_body, player_id, season_id)
            list_of_all_seasons.append(stats_lists)
    return list_of_all_seasons
