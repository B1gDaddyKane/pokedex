DROP TABLE IF EXISTS pokemon;
DROP TABLE IF EXISTS trainer;

CREATE TABLE pokemon
(
    pokeid INTEGER PRIMARY KEY,
    pokename TEXT UNIQUE NOT NULL,
    firsttype TEXT NOT NULL,
    secondtype TEXT,
    hp INTEGER,
    atk INTEGER,
    def INTEGER,
    sp_atk INTEGER,
    sp_def INTEGER,
    speed INTEGER
);

CREATE TABLE trainer
(
    id INTEGER PRIMARY KEY,
    trainername TEXT UNIQUE NOT NULL,
    pass TEXT NOT NULL
);