-- public.reservas_cancha definition

-- Drop table

-- DROP TABLE public.reservas_cancha;

CREATE TABLE reserva_futbol.public.reservas_cancha (
	id int8 GENERATED BY DEFAULT AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE) NOT NULL,
	nombre varchar(100) NOT NULL,
	ubicacion varchar(255) NOT NULL,
	CONSTRAINT reservas_cancha_pkey PRIMARY KEY (id)
);