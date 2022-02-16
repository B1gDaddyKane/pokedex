DROP TABLE IF EXISTS pokemon;
DROP TABLE IF EXISTS trainer;

CREATE TABLE pokemon
(
    id INTEGER PRIMARY KEY,
    pokeid INTEGER,
    pokename TEXT UNIQUE NOT NULL,
    poketype TEXT NOT NULL
);

CREATE TABLE trainer
(
    id INTEGER PRIMARY KEY,
    trainername TEXT UNIQUE NOT NULL,
    pass TEXT NOT NULL
);