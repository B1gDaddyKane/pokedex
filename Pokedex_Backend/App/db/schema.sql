DROP TABLE IF EXISTS pokemon;
DROP TABLE IF EXISTS trainer;

CREATE TABLE pokemon
(
    pokeid INTEGER PRIMARY KEY,
    pokename TEXT UNIQUE NOT NULL,
    firsttype TEXT NOT NULL,
    secondtype TEXT
);

CREATE TABLE trainer
(
    id INTEGER PRIMARY KEY,
    trainername TEXT UNIQUE NOT NULL,
    pass TEXT NOT NULL
);