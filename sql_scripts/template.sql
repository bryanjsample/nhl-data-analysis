CREATE DATABASE nhlStats;


USE nhlStats;


CREATE TABLE players (
	playerId VARCHAR(15) PRIMARY KEY,
	firstName VARCHAR(20),
    lastName CHAR(20),
    pos VARCHAR(10),
    handedness CHAR(1),
    heightInches INT,
    weightLbs INT,
    birthdate VARCHAR(10),
    birthLocationPrimary VARCHAR(30),
    birthLocationSecondary VARCHAR(30),
    birthCountry CHAR(2)
    );

CREATE TABLE seasons (
	seasonId VARCHAR(10) PRIMARY KEY,
    seasonStart DATE,
    seasonEnd DATE
    );

CREATE TABLE teams (
	team CHAR(10) PRIMARY KEY
	);

CREATE TABLE assists (
	playerId VARCHAR(15) NOT NULL,
    seasonId VARCHAR(10) NOT NULL,
    team CHAR (10) NOT NULL,
    evenStrengthAssists INT,
    powerPlayAssists INT,
    shorthandedAssists INT,
    PRIMARY KEY(playerId, seasonId, team),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId),
    FOREIGN KEY(team) REFERENCES teams(team)
    );

CREATE TABLE goalieStats (
	playerId VARCHAR(15) NOT NULL,
    seasonId VARCHAR(10) NOT NULL,
    team CHAR (10) NOT NULL,
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
    PRIMARY KEY(playerId, seasonId, team),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId),
    FOREIGN KEY(team) REFERENCES teams(team)
    );

CREATE TABLE goals (
	playerId VARCHAR(15) NOT NULL,
    seasonId VARCHAR(10) NOT NULL,
    team CHAR (10) NOT NULL,
	evenStrengthGoals INT,
    powerPlayGoals INT,
    shorthandedGoals INT,
    gameWinningGoals INT,
    PRIMARY KEY(playerId, seasonId, team),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId),
    FOREIGN KEY(team) REFERENCES teams(team)
    );
    
CREATE TABLE miscStats (
	playerId VARCHAR(15) NOT NULL,
    seasonId VARCHAR(10) NOT NULL,
    team CHAR (10) NOT NULL,
    penaltyMinutes INT,
    timeOnIce INT,
    averageTimeOnIce VARCHAR(10),
    faceoffWins INT,
    faceoffLosses INT,
    shotsBlocked INT,
    hits INT,
    takeaways INT,
    giveaways INT,
    PRIMARY KEY(playerId, seasonId, team),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId),
    FOREIGN KEY(team) REFERENCES teams(team)
    );

CREATE TABLE scoring (
	playerId VARCHAR(15) NOT NULL,
    seasonId VARCHAR(10) NOT NULL,
    team CHAR (10) NOT NULL,
	goals INT,
    assists INT,
    points INT,
	plusMinus INT,
    PRIMARY KEY(playerId, seasonId, team),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId),
    FOREIGN KEY(team) REFERENCES teams(team)
    );

CREATE TABLE seasonInfo (
	playerId VARCHAR(15) NOT NULL,
    seasonId VARCHAR(10) NOT NULL,
    team CHAR (10) NOT NULL,
	age INT,
    league VARCHAR(10),
    gamesPlayed INT,
    PRIMARY KEY(playerId, seasonId, team),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId),
    FOREIGN KEY(team) REFERENCES teams(team)
    );

CREATE TABLE shots (
	playerId VARCHAR(15) NOT NULL,
    seasonId VARCHAR(10) NOT NULL,
    team CHAR (10) NOT NULL,
	shotsOnGoal INT,
    totalShotsAttempted INT,
    PRIMARY KEY(playerId, seasonId, team),
    FOREIGN KEY(playerId) REFERENCES players(playerId),
    FOREIGN KEY(seasonId) REFERENCES seasons(seasonId),
    FOREIGN KEY(team) REFERENCES teams(team)
    );
