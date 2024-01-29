from bs4 import BeautifulSoup
import requests
from time import sleep

def form_list_of_alphabet_urls():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_url_list = []
    for letter in alphabet:
        url = f'https://www.hockey-reference.com/players/{letter}/'
        alphabet_url_list.append(url)
    return alphabet_url_list

def form_list_of_player_urls_and_ids(alphabet_url):
    player_url_and_id_list = []
    letter = alphabet_url[-2]
    base_url = alphabet_url.replace(f'/players/{letter}/', '')
    sleep(4)
    req = requests.get(alphabet_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    player_url_div = soup.find('div', id = 'div_players')
    player_p_list = player_url_div.find_all('p', class_ = 'nhl')
    for player_p in player_p_list:
        player_a = player_p.find('a')
        player_shortened_url = player_a.get('href')
        player_id = player_shortened_url.replace('.html', '')
        player_id = '"' + player_id.replace(f'/players/{letter}/', '') + '"'
        player_url = base_url + player_shortened_url
        player_dict = {player_id : player_url}
        player_url_and_id_list.append(player_dict)
    print(player_url_and_id_list)
    return player_url_and_id_list