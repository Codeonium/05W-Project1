DROP TABLE IF EXISTS keikos;
DROP TABLE IF EXISTS senseis;
DROP TABLE IF EXISTS dechis;

CREATE TABLE dechis (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    level INT,
    -- knowledge VARCHAR(255) i Want this to be a list must look for how
)

CREATE TABLE senseis (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    level INT,
    -- knowledge VARCHAR(255) i Want this to be a list must look for how
)

CREATE TABLE keikos (
    id SERIAL PRIMARY KEY,
    sensei_id INT REFERENCES senseis(id) ON DELETE CASCADE,
    -- time // i want this to display a 24hours time
    space INT,
    level INT REFERENCES senseis(level) ON DELETE CASCADE,
    attendance INT REFERENCES deshis(id) ON DELETE CASCADE
)