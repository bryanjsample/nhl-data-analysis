'''
Script to scrape data from all NHL players in the hockey-reference.com database

Author: Bryan Sample

Date: 1/20/24
'''

import form_urls
import scrape_stats
import database_and_sql

def main():
    database_and_sql.check_if_db_exists()
    last_entry = database_and_sql.determine_last_entry()
    database_and_sql.populate_seasons_table()
    alphabet_url_list = form_urls.form_list_of_alphabet_urls(last_entry)
    print(alphabet_url_list)
    for alphabet_url in alphabet_url_list:
        # find all players listed under each letter
        player_url_and_id_list = form_urls.form_list_of_player_urls_and_ids(alphabet_url, last_entry)

        # obtain list of dictionaries
        for player in player_url_and_id_list:
            # obtain key value pairs from  each dictionary
            for player_id, player_url in player.items():
                # obtain table data and add into databases
                player_list_and_all_seasons = scrape_stats.find_web_elements(player_url, player_id)
                database_and_sql.add_data_to_database(player_list_and_all_seasons)

if __name__ == '__main__':
    main()