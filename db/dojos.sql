DROP TABLE IF EXISTS keikos;
DROP TABLE IF EXISTS senseis;
DROP TABLE IF EXISTS deshis;
DROP TABLE IF EXISTS wazas;

CREATE TABLE wazas (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE deshis (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    waza_id INT REFERENCES wazas(id) ON DELETE CASCADE
);

CREATE TABLE senseis (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    waza_id INT REFERENCES wazas(id) ON DELETE CASCADE
);

CREATE TABLE keikos (
    id SERIAL PRIMARY KEY,
    sensei_id INT REFERENCES senseis(id),
    time TIME,
    deshi_id INT REFERENCES deshis(id)
);