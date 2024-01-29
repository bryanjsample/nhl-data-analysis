USE nhlStats;

CREATE TABLE assists (
	playerId VARCHAR(9) NOT NULL,
    seasonId VARCHAR(7) NOT NULL,
	totalAssists INT,
    evenStrengthAssists INT,
    powerPlayAssists INT,
    shorthandedAssists INT,
    PRIMARY KEY (playerId, seasonId),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId)
    );

DESCRIBE assists;
