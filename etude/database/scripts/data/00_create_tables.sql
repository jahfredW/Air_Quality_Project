-- object: public.departement | type: TABLE --
DROP TABLE IF EXISTS public.departement CASCADE;
CREATE TABLE public.departement (
	departement_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	departement_code varchar(5) NOT NULL,
	departement_nom varchar(30) NOT NULL,
	CONSTRAINT departement_pk PRIMARY KEY (departement_id)

);
-- ddl-end --
ALTER TABLE public.departement OWNER TO dev;
-- ddl-end --

-- object: public.ville | type: TABLE --
DROP TABLE IF EXISTS public.ville CASCADE;
CREATE TABLE public.ville (
	ville_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	ville_nom varchar(30) NOT NULL,
	ville_code_postal integer NOT NULL,
	departement_id smallint,
	CONSTRAINT ville_pk PRIMARY KEY (ville_id)

);
-- ddl-end --
ALTER TABLE public.ville OWNER TO dev;
-- ddl-end --

-- object: departement_fk | type: CONSTRAINT --
ALTER TABLE public.ville DROP CONSTRAINT IF EXISTS departement_fk CASCADE;
ALTER TABLE public.ville ADD CONSTRAINT departement_fk FOREIGN KEY (departement_id)
REFERENCES public.departement (departement_id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.pollution | type: TABLE --
DROP TABLE IF EXISTS public.pollution CASCADE;
CREATE TABLE public.pollution (
	pollution_id smallint NOT NULL GENERATED ALWAYS AS IDENTITY ,
	aqi integer NOT NULL,
	co decimal(5,2),
	no decimal(5,2),
	no2 decimal(5,2),
	"O3" decimal(5,2),
	"SO2" decimal(5,2),
	pm2_5 decimal(5,2),
	pm10 decimal(5,2),
	nh3 decimal(5,2),
	day date NOT NULL,
	last_update date NOT NULL,
	id_ville integer NOT NULL,
	ville_id smallint,
	CONSTRAINT pollution_pk PRIMARY KEY (pollution_id)

);
-- ddl-end --
COMMENT ON COLUMN public.pollution.co IS E'monoxyde de carbone';
-- ddl-end --
COMMENT ON COLUMN public.pollution.no IS E'nitrogen';
-- ddl-end --
COMMENT ON COLUMN public.pollution.no2 IS E'nitrogene (dioxyde)';
-- ddl-end --
COMMENT ON COLUMN public.pollution."O3" IS E'Ozone';
-- ddl-end --
COMMENT ON COLUMN public.pollution."SO2" IS E'dioxyde de sulphure';
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
ALTER TABLE public.pollution ADD CONSTRAINT ville_fk FOREIGN KEY (ville_id)
REFERENCES public.ville (ville_id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --