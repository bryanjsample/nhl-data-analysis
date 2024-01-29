USE nhlStats;

CREATE TABLE goals (
	playerId VARCHAR(9) NOT NULL,
    seasonId VARCHAR(7) NOT NULL,
    totalGoals INT,
	evenStrengthGoals INT,
    powerPlayGoals INT,
    shorthandedGoals INT,
    gameWinningGoals INT,
    PRIMARY KEY(playerID, seasonID),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId)
    );
    
DESCRIBE goals;

DROP TABLE goals;