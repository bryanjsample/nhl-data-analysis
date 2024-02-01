from time import sleep
import requests
from bs4 import BeautifulSoup
import database_and_sql

def sort_player_info(soup, player_url, player_id):
    # find player name
    name = soup.find('h1').get_text()
    while 'Error code' in name:
        sleep(10)
        req = requests.get(player_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        name = soup.find('h1').get_text()
    name = name.replace('\n', '')
    name_list = name.split(sep = ' ')
    if len(name_list) > 2:
        first_name = '"' + name_list[0] + '"'
        last_name = '"'
        for i in name_list[1:]:
            last_name += i + ' '
        last_name = last_name[:-1]
        last_name+= '"'
    else:
        first_name = '"' + name_list[0] + '"'
        last_name = '"' + name_list[-1] + '"'
    print(f'\n\nName: {first_name} {last_name}')

    # find player info
    info_div = soup.find('div', id = 'meta')
    info_p_list = info_div.find_all('p')

    # initialize variables in case they dont exist
    position = None
    handedness = None
    birthdate = None
    birth_location_primary = None
    birth_location_secondary = None
    birth_country = None
    height_inches = None
    weight_lbs = None

    for info_p in info_p_list:
        info = info_p.get_text()

        # find position and shooting hand
        if 'Position:' in info and 'Shoots:' in info:
            pos_shoot_list = info.split('•')
            for item in pos_shoot_list:
                if 'Position:' in item:
                    position = item.replace('Position:', '')
                    position = position.replace(' ', '')
                    position = '"' + position.replace('\xa0', '') + '"'
                    print(f'Position:{position}')
                if 'Shoots:' in item:
                    handedness = item.replace('Shoots:', '')
                    handedness = handedness.replace(' ', '')
                    handedness = '"' + handedness[1] + '"'

        # if goalie, then find catching hand
        elif 'Position:' in info and 'Catches:' in info:
            pos_catches_list = info.split('•')
            for item in pos_catches_list:
                if 'Position:' in item:
                    position = item.replace('Position:', '')
                    position = position.replace(' ', '')
                    position = '"' + position.replace('\xa0', '') + '"'
                    print(f'Position:{position}')
                if 'Catches:' in item:
                    handedness = item.replace('Catches:', '')
                    handedness = handedness.replace(' ', '')
                    handedness = '"' + handedness[1] + '"'
                    print(f'Catches:{handedness}')
        
        # if no handedness is listed
        elif 'Position:' in info:
            if 'Catches:' not in info and 'Shoots:' not in info:
                position = info.replace('Position:', '')
                position = position.replace(' ', '')
                position = '"' + position.replace('\n', '') + '"'
                handedness = 'NULL'
            else:
                print('Something real weird is happening.')
        
        # find birth details
        elif 'Born:' in info:
            birth_details_list = []
            birth_details_elements = info_p.find_all('span')
            for details_element in birth_details_elements:
                details = details_element.get_text()
                if '&nbsp;' in details:
                    details = details.replace('&nbsp;', '')
                if '\xa0' in details:
                    details = details.replace('\xa0', ' ')
                if ' in ' in details:
                    details = details.replace(' in ', '')
                if len(details) > 0:
                    if details[0] == ' ':
                        details = details[1:]
                birth_details_list.append(details)
            # if all birth details are present
            if len(birth_details_list) == 3:
                # find birthdate
                full_birthdate = birth_details_list[0].replace(',', '')
                birthdate_items = full_birthdate.split(' ')
                birth_month = determine_numeric_month(birthdate_items[0])
                birth_day = birthdate_items[1]
                if len(birth_day) ==1:
                    birth_day = '0' + birth_day
                birth_year = birthdate_items[2]
                birthdate = f'"{birth_year}-{birth_month}-{birth_day}"'

                # find birth location (city and country / state / province)
                birth_location_items = birth_details_list[1].split(',',)
                if len(birth_location_items) == 1:
                    birth_location_primary = "NULL"
                    birth_location_secondary = f'"{birth_location_items[0].strip()}"'
                else:
                    birth_location_primary = f'"{birth_location_items[0].strip()}"'
                    birth_location_secondary = f'"{birth_location_items[1].strip()}"'

                #find birth country code
                birth_country = '"' + birth_details_list[2].upper() + '"'

        # find height and weight
        elif 'lb' in info and 'cm' in info and 'kg' in info:
            for index, character in enumerate(info):
                # clean string
                if character == '(':
                    remove_index = index
            full_height_weight = info[:remove_index - 1]
            height_weight = full_height_weight.replace(' ', '')
            height_weight_list = height_weight.split(',')

            # if all components are present
            if len(height_weight_list) == 2:
                # find height in inches
                height_items = height_weight_list[0].split('-')
                height_inches = str((int(height_items[0]) * 12) + int(height_items[1]))

                # find weight
                if 'lbs' in height_weight_list[1]:
                    weight_lbs = height_weight_list[1].replace('lbs', '')
                    weight_lbs = weight_lbs.replace('\xa0', '')
                elif 'lb' in height_weight_list[1]:
                    weight_lbs = height_weight_list[1].replace('lb', '')
                    weight_lbs = weight_lbs.replace('\xa0', '')
                elif 'kgs' in height_weight_list[1]:
                    weight_kgs = height_weight_list[1].replace('kgs', '')
                    weight_kgs = weight_kgs.replace('\xa0', '')
                    weight_lbs = str(int(round((float(weight_kgs) * 2.20462), ndigits = 0)))
                elif 'kg' in height_weight_list[1]:
                    weight_kgs = height_weight_list[1].replace('kg', '')
                    weight_kgs = weight_kgs.replace('\xa0', '')
                    weight_lbs = str(int(round((float(weight_kgs) * 2.20462), ndigits = 0)))
                else:
                    print('Something went wrong finding the weight')
            

    # form list of dictionaries for player database
    player_list = {'players' : (
        {'playerId' : player_id},
        {'firstName' : first_name},
        {'lastName' : last_name},
        {'pos' : position},
        {'handedness' : handedness},
        {'birthdate' : birthdate},
        {'birthLocationPrimary' : birth_location_primary},
        {'birthLocationSecondary' : birth_location_secondary},
        {'birthCountry' : birth_country},
        {'heightInches' : height_inches},
        {'weightLbs' : weight_lbs}
        )
        }
    
    return player_list

def sort_player_stats(stat_column_body, player_id, season_id):
    season_info_list = []
    misc_stats_list = []
    scoring_list = []
    goals_list = []
    assists_list = []
    shots_list = []

    # add player id and season id to beginning of every list
    for list in [season_info_list, misc_stats_list, scoring_list, goals_list, assists_list, shots_list]:
        list.append({'playerId' : player_id})
        list.append({'seasonId' : season_id})

    for column in stat_column_body: # iterate through stats
        # age
        if column.get('data-stat') == 'team_id':
            team = column.get_text()
            season_info_list.append({'team' : f'"{team}"'})
            misc_stats_list.append({'team' : f'"{team}"'})
            scoring_list.append({'team' : f'"{team}"'})
            goals_list.append({'team' : f'"{team}"'})
            assists_list.append({'team' : f'"{team}"'})
            shots_list.append({'team' : f'"{team}"'})
            database_and_sql.add_team_to_database(f'"{team}"')
            team = True
        # team
        elif column.get('data-stat') == 'age':
            age = column.get_text()
            season_info_list.append({'age' : age})
        # league
        elif column.get('data-stat') == 'lg_id':
            league = column.get_text()
            season_info_list.append({'league' : f'"{league}"'})
        # games played
        elif column.get('data-stat') == 'games_played':
            games_played = column.get_text()
            season_info_list.append({'gamesPlayed' : games_played})
        # goals
        elif column.get('data-stat') == 'goals':
            total_goals = column.get_text()
            scoring_list.append({'goals' : total_goals})
        # assists
        elif column.get('data-stat') == 'assists':
            total_goals = column.get_text()
            scoring_list.append({'assists' : total_goals})
        # points
        elif column.get('data-stat') == 'points':
            points = column.get_text()
            scoring_list.append({'points' : points})
        # plus minus
        elif column.get('data-stat') == 'plus_minus':
            plus_minus = column.get_text()
            scoring_list.append({'plusMinus' : plus_minus})
        # even strength goals
        elif column.get('data-stat') == 'goals_ev':
            even_strength_goals = column.get_text()
            goals_list.append({'evenStrengthGoals' : even_strength_goals})
        # power play goals
        elif column.get('data-stat') == 'goals_pp':
            power_play_goals = column.get_text()
            goals_list.append({'powerPlayGoals' : power_play_goals})
        # shorthanded goals
        elif column.get('data-stat') == 'goals_sh':
            shorthanded_goals = column.get_text()
            goals_list.append({'shorthandedGoals' : shorthanded_goals})
        # game winning goals
        elif column.get('data-stat') == 'goals_gw':
            game_winning_goals = column.get_text()
            goals_list.append({'gameWinningGoals' : game_winning_goals})
        # even strength assists
        elif column.get('data-stat') == 'assists_ev':
            even_strength_assists = column.get_text()
            assists_list.append({'evenStrengthAssists' : even_strength_assists})
        # powerplay assists
        elif column.get('data-stat') == 'assists_pp':
            power_play_assists = column.get_text()
            assists_list.append({'powerPlayAssists' : power_play_assists})
        # shorthanded assists
        elif column.get('data-stat') == 'assists_sh':
            shorthanded_assists = column.get_text()
            assists_list.append({'shorthandedAssists' : shorthanded_assists})
        # shots
        elif column.get('data-stat') == 'shots':
            shots = column.get_text()
            shots_list.append({'shotsOnGoal' : shots})
        # shots attempted
        elif column.get('data-stat') == 'shots_attempted':
            total_shots_attempted = column.get_text()
            shots_list.append({'totalShotsAttempted' : total_shots_attempted})
        # penalty minutes
        elif column.get('data-stat') == 'pen_min':
            penalty_minutes = column.get_text()
            misc_stats_list.append({'penaltyMinutes' : penalty_minutes})
        # time on ice
        elif column.get('data-stat') == 'time_on_ice':
            time_on_ice = column.get_text()
            misc_stats_list.append({'timeOnIce' : time_on_ice})
        # average time on ice
        elif column.get('data-stat') == 'time_on_ice_avg':
            average_time_on_ice = column.get_text()
            misc_stats_list.append({'averageTimeOnIce' : f'"{average_time_on_ice}"'})
        # faceoff wins
        elif column.get('data-stat') == 'faceoff_wins':
            faceoff_wins = column.get_text()
            misc_stats_list.append({'faceoffWins' : faceoff_wins})
        # faceoff losses
        elif column.get('data-stat') == 'faceoff_losses':
            faceoff_losses = column.get_text()
            misc_stats_list.append({'faceoffLosses' : faceoff_losses})
        # blocked shots
        elif column.get('data-stat') == 'blocks':
            blocked_shots = column.get_text()
            misc_stats_list.append({'shotsBlocked' : blocked_shots})
        # hits
        elif column.get('data-stat') == 'hits':
            hits = column.get_text()
            misc_stats_list.append({'hits' : hits})
        # takeaways
        elif column.get('data-stat') == 'takeaways':
            takeaways = column.get_text()
            misc_stats_list.append({'takeaways' : takeaways})
        # giveaways
        elif column.get('data-stat') == 'giveaways':
            giveaways = column.get_text()
            misc_stats_list.append({'giveaways' : giveaways})

    if team != True:
        team = 'na'
        database_and_sql.add_team_to_database(f'"{team}"')
        season_info_list.append({'team' : f'"{team}"'})
        misc_stats_list.append({'team' : f'"{team}"'})
        scoring_list.append({'team' : f'"{team}"'})
        goals_list.append({'team' : f'"{team}"'})
        assists_list.append({'team' : f'"{team}"'})
        shots_list.append({'team' : f'"{team}"'})

    stats_lists = [{'season_info_list' : season_info_list}, {'misc_stats_list' : misc_stats_list}, {'scoring_list' : scoring_list}, {'goals_list' : goals_list}, {'assists_list' : assists_list}, {'shots_list' : shots_list}]
    for stat_list in stats_lists:
        for key, value in stat_list.items():
            if len(value) <= 2:
                stats_lists.pop(stats_lists.index(stat_list))
    return stats_lists

def sort_goalie_stats(stat_column_body, player_id, season_id):
    season_info_list = []
    goalie_stats_list = []
    
    # add player and season id to list
    for list in [season_info_list, goalie_stats_list]:
        list.append({'playerId' : player_id})
        list.append({'seasonId' : season_id})

    # iterate through stats
    for column in stat_column_body: 
        # team
        if column.get('data-stat') == 'team_id':
            team = column.get_text()
            season_info_list.append({'team' : f'"{team}"'})
            goalie_stats_list.append({'team' : f'"{team}"'})
            database_and_sql.add_team_to_database(f'"{team}"')
            team = True
        # age
        elif column.get('data-stat') == 'age':
            age = column.get_text()
            season_info_list.append({'age' : age})
        # league
        elif column.get('data-stat') == 'lg_id':
            league = column.get_text()
            season_info_list.append({'league' : f'"{league}"'})
        # games played
        elif column.get('data-stat') == 'games_goalie':
            games_played = column.get_text()
            season_info_list.append({'gamesPlayed' : games_played})
        # games started
        elif column.get('data-stat') == 'starts_goalie':
            games_started = column.get_text()
            goalie_stats_list.append({'gamesStarted' : games_started})
        # wins
        elif column.get('data-stat') == 'wins_goalie':
            wins = column.get_text()
            goalie_stats_list.append({'wins' : wins})
        # losses
        elif column.get('data-stat') == 'losses_goalie':
            losses = column.get_text()
            goalie_stats_list.append({'losses' : losses})
        # ties / otl
        elif column.get('data-stat') == 'ties_goalie':
            ties_otl = column.get_text()
            goalie_stats_list.append({'tieOtlSol' : ties_otl})
        # goals against
        elif column.get('data-stat') == 'goals_against':
            goals_against = column.get_text()
            goalie_stats_list.append({'goalsAgainst' : goals_against})
        # shots against
        elif column.get('data-stat') == 'shots_against':
            shots_against = column.get_text()
            goalie_stats_list.append({'shotsAgainst' : shots_against})
        # saves
        elif column.get('data-stat') == 'saves':
            saves = column.get_text()
            goalie_stats_list.append({'saves' : saves})
        # shutouts
        elif column.get('data-stat') == 'shutouts':
            shutouts = column.get_text()
            goalie_stats_list.append({'shutouts' : shutouts})
        # minutes
        elif column.get('data-stat') == 'min_goalie':
            minutes = column.get_text()
            goalie_stats_list.append({'minutes' : minutes})
        # goalie point share
        elif column.get('data-stat') == 'gps':
            goalie_point_share = column.get_text()
            goalie_stats_list.append({'goaliePointShare' : goalie_point_share})
        # goals
        elif column.get('data-stat') == 'goals':
            goals = column.get_text()
            goalie_stats_list.append({'goals' : goals})
        # assists
        elif column.get('data-stat') == 'assists':
            assists = column.get_text()
            goalie_stats_list.append({'assists' : assists})
        # points
        elif column.get('data-stat') == 'points':
            points = column.get_text()
            goalie_stats_list.append({'points' : points})
        # penalty minutes
        elif column.get('data-stat') == 'pen_min':
            penalty_minutes = column.get_text()
            goalie_stats_list.append({'penaltyMinutes' : penalty_minutes})

    if team != True:
        team = 'na'
        database_and_sql.add_team_to_database(f'"{team}"')
        season_info_list.append({'team' : f'"{team}"'})
        goalie_stats_list.append({'team' : f'"{team}"'})

    stats_lists = [{'season_info_list' : season_info_list}, {'goalie_stats_list' : goalie_stats_list}]
    return stats_lists

def determine_numeric_month(birthdate_item):
    if birthdate_item == 'January':
        birth_month = '01'
    elif birthdate_item == 'February':
        birth_month = '02'
    elif birthdate_item == 'March':
        birth_month = '03'
    elif birthdate_item == 'April':
        birth_month = '04'
    elif birthdate_item == 'May':
        birth_month = '05'
    elif birthdate_item == 'June':
        birth_month = '06'
    elif birthdate_item == 'July':
        birth_month = '07'
    elif birthdate_item == 'August':
        birth_month = '08'
    elif birthdate_item == 'September':
        birth_month = '09'
    elif birthdate_item == 'October':
        birth_month = '10'
    elif birthdate_item == 'November':
        birth_month = '11'
    elif birthdate_item == 'December':
        birth_month = '12'
    return birth_month