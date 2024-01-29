USE nhl_stats;

CREATE TABLE example (
	player_id VARCHAR(9) NOT NULL,
    season_id VARCHAR(7) NOT NULL,
	
    FOREIGN KEY(player_id) REFERENCES players(player_id),
    FOREIGN KEY(season_id) REFERENCES seasons(season_id)
    );
