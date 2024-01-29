USE nhlStats;

CREATE TABLE players (
	playerId VARCHAR(9) PRIMARY KEY,
	firstName VARCHAR(20),
    lastName CHAR(20),
    pos CHAR(2),
    handedness CHAR(1),
    heightInches INT,
    weightLbs INT,
    birthdate VARCHAR(10),
    birthLocationPrimary VARCHAR(30),
    birthLocationSecondary VARCHAR(30),
    birthCountry CHAR(2)
    );

DESCRIBE players;

SELECT * FROM players;
