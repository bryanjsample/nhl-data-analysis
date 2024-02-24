from bs4 import BeautifulSoup
import requests

def scrape_list_of_seasons():
    url = 'https://www.hockey-reference.com/leagues/'

    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    table_body = soup.find('table', id = 'league_index').find('tbody').find_all('tr')

    season_links = []
    seasons = {}

    for row in table_body:
        season_links.append(row.find('th').find('a').get('href'))
        seasonId = row.find('th').get_text()
        if seasonId == '2023-24':
            seasons[seasonId] = {
            'stanleyCupChampion' : None,
            'stanleyCupRunnerUp' : None, 
            'hartTrophyWinner' : None, 
            'vezinaTrophyWinner' : None, 
            'calderTrophyWinner' : None, 
            'norrisTrophyWinner' : None, 
            'connSmytheTrophyWinner' : None
            }
        else:
            season_stats = sort_season_stats(row)
            seasons[seasonId] = season_stats
            if seasonId == '2005-06':
                break

    return [season_links, seasons]


def sort_season_stats(row):
    season = row.find_all('td')
    for stat in season:
        if stat.get('data-stat') == 'champion':
            stanleyCupChampion = strip_team_id(stat)
        elif stat.get('data-stat') == 'runnerup':
            stanleyCupRunnerUp = strip_team_id(stat)
        elif stat.get('data-stat') == 'hart_winner_name':
            hartTrophyWinner = strip_player_id(stat)
        elif stat.get('data-stat') == 'vezina_winner_name':
            vezinaTrophyWinner = strip_player_id(stat)
        elif stat.get('data-stat') == 'calder_winner_name':
            calderTrophyWinner = strip_player_id(stat)
        elif stat.get('data-stat') == 'norris_winner_name':
            norrisTrophyWinner = strip_player_id(stat)
        elif stat.get('data-stat') == 'smythe_winner_name':
            connSmytheTrophyWinner = strip_player_id(stat)
    return {
            'stanleyCupChampion' : stanleyCupChampion,
            'stanleyCupRunnerUp' : stanleyCupRunnerUp, 
            'hartTrophyWinner' : hartTrophyWinner, 
            'vezinaTrophyWinner' : vezinaTrophyWinner, 
            'calderTrophyWinner' : calderTrophyWinner, 
            'norrisTrophyWinner' : norrisTrophyWinner, 
            'connSmytheTrophyWinner' : connSmytheTrophyWinner
            }

def strip_team_id(stat):
    href = stat.find('a').get('href')
    split_href = href.split(sep = '/')
    return split_href[split_href.index('teams') + 1]

def strip_player_id(stat):
    href = stat.find('a').get('href')
    split_href = href.split(sep = '/')
    return split_href[-1].replace('.html', '')