-- object: public.ville | type: TABLE --
DROP TABLE IF EXISTS public.ville CASCADE;
CREATE TABLE public.ville (
	id_ville integer NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom varchar(60),
	id_departement smallint NOT NULL,
	code_postal integer NOT NULL,
	CONSTRAINT ville_pk PRIMARY KEY (id_ville)

);
-- ddl-end --
ALTER TABLE public.ville OWNER TO dev_role;
-- ddl-end --

-- object: public.prevision | type: TABLE --
DROP TABLE IF EXISTS public.prevision CASCADE;
CREATE TABLE public.prevision (
	id_prevision integer NOT NULL GENERATED ALWAYS AS IDENTITY ,
	temperature decimal(5,2) NOT NULL,
	temperature_min decimal(5,2),
	temperature_max decimal(5,2),
	temperature_matin decimal(5,2),
	temperature_apres_midi decimal(5,2),
	temperature_nuit decimal(5,2),
	description varchar(30) NOT NULL,
	direction_vent smallint,
	force_vent decimal(5,2),
	jour date NOT NULL,
	last_update date NOT NULL,
	id_ville integer NOT NULL,
	CONSTRAINT prevision_pk PRIMARY KEY (id_prevision)

);
-- ddl-end --
COMMENT ON COLUMN public.prevision.direction_vent IS E'en degrés';
-- ddl-end --
COMMENT ON COLUMN public.prevision.force_vent IS E'en km/h';
-- ddl-end --
ALTER TABLE public.prevision OWNER TO dev_role;
-- ddl-end --

-- object: public.departement | type: TABLE --
DROP TABLE IF EXISTS public.departement CASCADE;
CREATE TABLE public.departement (
	id_departement smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	nom varchar(50),
	code varchar(3) NOT NULL,
	CONSTRAINT departement_pk PRIMARY KEY (id_departement)

);

-- object: public.pollution.py | type: TABLE --
DROP TABLE IF EXISTS public.pollution CASCADE;
CREATE TABLE public.pollution (
	id_pollution smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	aqi integer ,
	co decimal(5,2),
	no decimal(5,2),
	no2 decimal(5,2),
	o3 decimal(5,2),
	so2 decimal(5,2),
	pm2_5 decimal(5,2),
	pm10 decimal(5,2),
	nh3 decimal(5,2),
	day date NOT NULL ,
	last_update date NOT NULL,
	id_ville integer NOT NULL,

	CONSTRAINT pollution_pk PRIMARY KEY (id_pollution)

);
-- ddl-end --
COMMENT ON COLUMN public.pollution.co IS E'monoxyde de carbone';
-- ddl-end --
COMMENT ON COLUMN public.pollution.no IS E'nitrogen';
-- ddl-end --
COMMENT ON COLUMN public.pollution.no2 IS E'nitrogene (dioxyde)';
-- ddl-end --
COMMENT ON COLUMN public.pollution.o3 IS E'Ozone';
-- ddl-end --
COMMENT ON COLUMN public.pollution.so2 IS E'dioxyde de sulphure';
-- ddl-end --
COMMENT ON COLUMN public.pollution.pm2_5 IS E'micro_particules d = 2.5\nen Microgrammes / m3';
-- ddl-end --
COMMENT ON COLUMN public.pollution.pm10 IS E'micro_particules d = 10\nen Microgrammes / m3';
-- ddl-end --
COMMENT ON COLUMN public.pollution.nh3 IS E'Amoniac\nMG / m3';
-- ddl-end --
ALTER TABLE public.pollution OWNER TO dev;
-- ddl-end --

-- object: ville_fk | type: CONSTRAINT --
ALTER TABLE public.pollution DROP CONSTRAINT IF EXISTS ville_fk CASCADE;
ALTER TABLE public.pollution ADD CONSTRAINT ville_fk FOREIGN KEY (id_ville)
REFERENCES public.ville (id_ville) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --
-- ddl-end --
ALTER TABLE public.departement OWNER TO dev_role;
-- ddl-end --

-- object: departement_fk | type: CONSTRAINT --
ALTER TABLE public.ville DROP CONSTRAINT IF EXISTS departement_fk CASCADE;
ALTER TABLE public.ville ADD CONSTRAINT departement_fk FOREIGN KEY (id_departement)
REFERENCES public.departement (id_departement) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: ville_fk | type: CONSTRAINT --
ALTER TABLE public.prevision DROP CONSTRAINT IF EXISTS ville_fk CASCADE;
ALTER TABLE public.prevision ADD CONSTRAINT ville_fk FOREIGN KEY (id_ville)
REFERENCES public.ville (id_ville) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


