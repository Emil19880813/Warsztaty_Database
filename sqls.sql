CREATE DATABASE communications_server;

CREATE TABLE Users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) unique,
  username VARCHAR(255),
  hashed_password VARCHAR(80)
);

CREATE TABLE Messages (
  id SERIAL PRIMARY KEY,
  from_id int,
  to_id int,
  text VARCHAR(255),
  creation_date VARCHAR(6)
);