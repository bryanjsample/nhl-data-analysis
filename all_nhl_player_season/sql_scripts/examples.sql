USE nhlStats


-- SELECT * FROM players;

-- SELECT * FROM seasons;

-- SELECT * FROM teams;

-- SELECT * FROM seasonInfo;

-- SELECT * FROM scoring;

-- SELECT * FROM goals;

-- SELECT * FROM assists;

-- SELECT * FROM shots;

-- SELECT * FROM miscStats;

-- SELECT * FROM goalieStats;

-- SELECT p.firstName as FirstName,
-- p.lastName as LastName,
-- p.birthLocationPrimary as City,
-- p.birthLocationSecondary as State,
-- p.birthCountry as Country
-- FROM players p
-- WHERE p.birthLocationSecondary IN ('Minnesota', 'Colorado')
-- ORDER BY p.birthLocationSecondary, p.birthLocationPrimary;

-- SELECT 
-- p.playerId as id,
-- p.firstName,
-- p.lastName,
-- s.seasonId,
-- s.goals,
-- s.assists,
-- s.points
-- FROM players p
-- INNER JOIN
-- scoring s
-- ON p.playerId = s.playerId
;

-- WHERE p.playerId = 'nichuva01'

-- SELECT 
-- p.playerId as id,
-- p.firstName as FirstName,
-- p.lastName as LastName,
-- p.pos as Position,
-- m.seasonId as Season,
-- m.penaltyMinutes as PIM,
-- m.timeOnIce as TOI,
-- m.faceoffWins as FOW,
-- m.faceoffLosses as FOL,
-- m.shotsBlocked as BlockedShots,
-- m.hits as Hits,
-- m.takeaways as Takeaways,
-- m.giveaways as Giveaways
-- FROM players p
-- INNER JOIN
-- miscStats m
-- ON p.playerId = m.playerId
-- ;