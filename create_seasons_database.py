import mysql.connector

def populate_seasons_table():
    #connect to database
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '8ad7fpx2!',
        database = 'nhlStats'
    )
    my_cursor = db.cursor()

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
        my_cursor.execute(f'INSERT INTO seasons (seasonId, seasonStart, seasonEnd) VALUES ("{season_key}", "{season_start}", "{season_end}")')
        db.commit()
