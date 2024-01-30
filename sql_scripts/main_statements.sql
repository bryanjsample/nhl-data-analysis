USE nhlStats;


DROP DATABASE nhlStats;



DESCRIBE teams;

SELECT * FROM teams;

SELECT * FROM players ORDER BY playerId DESC;

SELECT * FROM seasons;

DESCRIBE goalieStats;

SELECT * FROM goalieStats;

SELECT * FROM seasonInfo WHERE playerId = "aaltoan01";

SELECT * FROM scoring;

SELECT * FROM goals;

SELECT * FROM assists;

SELECT * FROM shots;

SELECT * FROM miscStats;

DROP DATABASE nhlStats