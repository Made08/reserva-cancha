#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER futbol_app REPLICATION LOGIN ENCRYPTED PASSWORD 'futbol_app';
	GRANT ALL PRIVILEGES ON DATABASE reserva_futbol TO futbol_app;
EOSQL
