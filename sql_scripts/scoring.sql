USE nhlStats;

CREATE TABLE scoring (
	playerId VARCHAR(9) NOT NULL,
    seasonId VARCHAR(7) NOT NULL,
	goals INT,
    assists INT,
    points INT,
	plusMinus INT,
    PRIMARY KEY(playerId, seasonId),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId)
    );

DESCRIBE scoring;

DROP TABLE scoring;