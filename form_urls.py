from bs4 import BeautifulSoup
import requests
from time import sleep

def form_list_of_alphabet_urls(last_entry):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_url_list = []
    if last_entry is not None:
        last_letter = last_entry[0]
        index = alphabet.index(last_letter)
        alphabet = alphabet[index:]

    for letter in alphabet:
        url = f'https://www.hockey-reference.com/players/{letter}/'
        alphabet_url_list.append(url)
    return alphabet_url_list

def form_list_of_player_urls_and_ids(alphabet_url, last_entry):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
        for alpha_letter in alphabet:
            if f'/players/{alpha_letter}/' in player_id:
                player_id = '"' + player_id.replace(f'/players/{alpha_letter}/', '') + '"'
        if player_id != f'"{last_entry}"':
            player_url = base_url + player_shortened_url
            player_dict = {player_id : player_url}
            player_url_and_id_list.append(player_dict)
        else:
            player_url_and_id_list.clear()
    if letter == 'z' and len(player_url_and_id_list) == 0:
            print('All players have been added to the database')
            quit()
    elif len(player_url_and_id_list) == 0:
        return None
    print(f'Starting with {player_url_and_id_list[0]}')
    return player_url_and_id_list