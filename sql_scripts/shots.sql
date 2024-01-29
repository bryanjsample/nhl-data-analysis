USE nhlStats;

CREATE TABLE shots (
	playerId VARCHAR(9) NOT NULL,
    seasonId VARCHAR(7) NOT NULL,
	shotsOnGoal INT,
    totalShotsAttempted INT,
    PRIMARY KEY(playerId, seasonId),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId)
    );

DESCRIBE shots;