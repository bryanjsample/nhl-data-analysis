USE nhlStats;

CREATE TABLE seasonInfo (
	playerId VARCHAR(9) NOT NULL,
    seasonId VARCHAR(7) NOT NULL,
	age INT,
    team VARCHAR(10),
    league VARCHAR(10),
    gamesPlayed INT,
    PRIMARY KEY(playerId, seasonId),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId)
    );

DESCRIBE seasonInfo;

SHOW TABLES;