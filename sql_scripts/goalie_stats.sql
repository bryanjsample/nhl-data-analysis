USE nhlStats;

CREATE TABLE goalieStats (
	playerId VARCHAR(9) NOT NULL,
    seasonId VARCHAR(7) NOT NULL,
    gamesPlayed INT,
	gamesStarted INT,
    wins INT,
    losses INT,
    tieOtlSol INT,
    goalsAgainst INT,
    shotsAgainst INT,
    saves INT,
    shutouts INT,
    minutes INT,
    goaliePointShare DECIMAL(6, 3),
    goals INT,
    assists INT,
    points INT,
    penaltyMinutes DECIMAL(6, 3),
    PRIMARY KEY(playerId, seasonId),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId)
    );

DESCRIBE goalieStats;
