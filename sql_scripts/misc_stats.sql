USE nhlStats;

CREATE TABLE miscStats (
	playerId VARCHAR(9) NOT NULL,
    seasonId VARCHAR(7) NOT NULL,
    penaltyMinutes DECIMAL(5, 3),
    timeOnIce DECIMAL(10, 3),
    averageTimeOnIce VARCHAR(10),
    faceoffWins INT,
    faceoffLosses INT,
    shotsBlocked INT,
    hits INT,
    takeaways INT,
    giveaways INT,
    PRIMARY KEY(playerID, seasonID),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId)
    );

DESCRIBE miscStats;

