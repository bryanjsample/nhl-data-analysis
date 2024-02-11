USE nhlStats

-- SELECT p.firstName as FirstName,
-- p.lastName as LastName,
-- p.birthLocationPrimary as City,
-- p.birthLocationSecondary as State,
-- p.birthCountry as Country
-- FROM players p
-- WHERE p.birthLocationSecondary IN ('Minnesota', 'Colorado');

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
-- WHERE p.lastName = 'Gretzky'
-- ;