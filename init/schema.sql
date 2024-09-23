CREATE DATABASE IF NOT EXISTS clean_database;

CREATE TABLE IF NOT EXISTS `clean_database`.`users`
(
    id BIGINT AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(256) NOT NULL,
    last_name VARCHAR(256) NOT NULL,
    age INT NOT NULL,

    primary key (id)
);
