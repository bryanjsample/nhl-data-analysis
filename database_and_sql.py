import mysql.connector

def add_data_to_database(player_list_and_all_seasons):
    player_commited = False

    list_of_all_seasons = player_list_and_all_seasons[1]

    for season in list_of_all_seasons: # iterating through seasons of a single player
        stat_dictionaries = [player_list_and_all_seasons[0]]
        for dictionary in season: # iterating through lists of database dictionaries from a single season
            for key, value in dictionary.items(): # iterating through key and value from a single database dictionary
                key = key
                list = value

            if key == 'season_info_list':
                season_info_dict = {'seasonInfo' : list}
                stat_dictionaries.append(season_info_dict)
            if key == 'misc_stats_list':
                misc_stats_dict = {'miscStats' : list}
                stat_dictionaries.append(misc_stats_dict)
            if key == 'scoring_list':
                scoring_dict = {'scoring' : list}
                stat_dictionaries.append(scoring_dict)
            if key == 'goals_list':
                goals_dict = {'goals' : list}
                stat_dictionaries.append(goals_dict)
            if key == 'assists_list':
                assists_dict = {'assists' : list}
                stat_dictionaries.append(assists_dict)
            if key == 'shots_list':
                shots_dict = {'shots' : list}
                stat_dictionaries.append(shots_dict)
            if key == 'goalie_stats_list':
                goalie_stats_dict = {'goalieStats' : list}
                stat_dictionaries.append(goalie_stats_dict)

        for stat_dict in stat_dictionaries:
            try:
                for key, value in stat_dict.items():
                    table = key
                    stat_list = value
                # switch to only add to players table once
                if table == 'players':
                    if player_commited == True:
                        continue
                sql_statement = build_sql_statement(table, stat_list)
                # instantiate database
                db = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    passwd = '8ad7fpx2!',
                    database = 'nhlStats'
                )
                my_cursor = db.cursor()
                my_cursor.execute(sql_statement)
                db.commit()
                my_cursor.close()
                db.close()
                # flip switch
                if table == 'players':
                    player_commited = True
            except Exception as e:
                print("\n ############# \n", type(e), e, "\n ############# \n")
                db.rollback()
                my_cursor.close()
                db.close()
                raise
    print(f'Successfully added to database.')

def build_sql_statement(table, list_of_dicts):
    table_columns = []
    table_values = []

    for dict in list_of_dicts:
        for key, value in dict.items():
            if value == '':
                continue
            elif value == None:
                continue
            elif value == '""':
                continue
            elif value == "''":
                continue
            table_columns.append(key)
            table_values.append(value)

    len_table_columns = len(table_columns)
    len_table_values = len(table_values)
    if len_table_columns != len_table_values:
        raise Exception
    sql_statement = f'INSERT INTO {table} ('
    for column in table_columns:
        if table_columns.index(column) != len_table_columns - 1:
            sql_statement += f'{column}' + ', '
        else:
            sql_statement += f'{column}'
    sql_statement += ') VALUES ('
    for value in table_values:
        if table_values.index(value) != len_table_values - 1:
            sql_statement += f'{value}' + ', '
        else:
            sql_statement += f'{value}'
    sql_statement += ')'
    if sql_statement[-3:] == ', )':
        sql_statement = sql_statement[:-3] + ')'
    elif sql_statement[-2:] == ',)':
        sql_statement = sql_statement[:-2] + ')'
    print(sql_statement)
    return sql_statement
    
def add_team_to_database(team_name):
    # instantiate database
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '8ad7fpx2!',
        database = 'nhlStats'
    )
    my_cursor = db.cursor()
    try:
        my_cursor.execute(f'INSERT INTO teams(team) VALUES({team_name})')
        db.commit()
        my_cursor.close()
        db.close()
    except:
        db.rollback()
        my_cursor.close()
        db.close()

def populate_seasons_table():
    years = range(1900,2025)
    for year in years:
        season_start = f'{year}-09-01'
        season_end = f'{year + 1}-07-01'
        if str(year)[0] == '1':
            shortened_end = f'{(year + 1) - 1900}'
            if len(shortened_end) == 1:
                shortened_end = '0' + shortened_end
            elif shortened_end == '100':
                shortened_end = '00'
            season_key = f'{year}-{shortened_end}'
        if str(year)[0] == '2':
            shortened_end = f'{(year + 1) - 2000}'
            if len(shortened_end) == 1:
                shortened_end = '0' + shortened_end
            elif shortened_end == '100':
                shortened_end = '00'
            season_key = f'{year}-{shortened_end}'
        try:
        #connect to database
            db = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                passwd = '8ad7fpx2!',
                database = 'nhlStats'
            )
            my_cursor = db.cursor()
            my_cursor.execute(f'INSERT INTO seasons (seasonId, seasonStart, seasonEnd) VALUES ("{season_key}", "{season_start}", "{season_end}")')
            my_cursor.close()
            db.commit()
            db.close()
        except:
            my_cursor.close()
            db.rollback()
            db.close

def determine_last_entry():
    #connect to database
    db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '8ad7fpx2!',
    database = 'nhlStats'
    )
    my_cursor = db.cursor()
    my_cursor.execute('SELECT playerId FROM players ORDER BY playerId DESC LIMIT 1')
    last_entry_id_tuple = my_cursor.fetchone()
    if last_entry_id_tuple is not None:
        last_entry_id = last_entry_id_tuple[0]
        my_cursor.close()
        db.close()
        return last_entry_id
    else:
         my_cursor.close()
         db.close()