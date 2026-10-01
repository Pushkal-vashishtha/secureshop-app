-- SecureShop data tier (PostgreSQL 18 on RDS)
-- Run as db_admin. The app_user password is generated separately and stored in
-- SSM Parameter Store at /secureshop/dev/app/db_password - never in this file.

REVOKE ALL ON DATABASE secureshop FROM PUBLIC;
-- CREATE USER app_user WITH PASSWORD '<generated, see Parameter Store>';
GRANT CONNECT ON DATABASE secureshop TO app_user;

CREATE SCHEMA IF NOT EXISTS shop AUTHORIZATION db_admin;
GRANT USAGE ON SCHEMA shop TO app_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA shop GRANT SELECT, INSERT ON TABLES TO app_user;

CREATE TABLE IF NOT EXISTS shop.products (
    id         serial PRIMARY KEY,
    name       text    NOT NULL,
    price_inr  numeric NOT NULL
);
GRANT USAGE ON SEQUENCE shop.products_id_seq TO app_user;
