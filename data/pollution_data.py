from datetime import date

import psycopg2

HOST = "localhost"
DATABASE = "test2"
USER = "dev"
PASSWORD = "Farte512!"
PORT = 5432

def connect():
    try:
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
        cursor = connection.cursor()
        print('Version du serveur PostgreSQL:')
        cursor.execute("SELECT * from departement")

        departements = cursor.fetchall()
        print(departements)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print('connection à la BDD fermée')

def get_id_ville(nom_ville: str):
    sql = "select id_ville from ville where nom = '{0}'".format(nom_ville);

    try:
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
        cursor = connection.cursor()
        cursor.execute(sql)

        row = cursor.fetchall()
        connection.commit()
        cursor.close()

        return row

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()
            print('connection à la BDD fermée')

def ville_exists(ville: str):
    sql = "SELECT id_ville from ville where nom='{}'".format(ville)

    connection = None
    try:
        connection = psycopg2.connect(host=HOST, database=DATABASE, user= USER, password=PASSWORD, port=PORT)
        cursor = connection.cursor()

        cursor.execute(sql)
        row = cursor.fetchone()

        connection.commit()
        cursor.close()

        if row is not None:
            return True
        return False

    except (Exception, psycopg2.DatabaseError) as error:
        print("error ville exits")
        print(error)

    finally:
        if connection is not None:
            connection.close()


def ajout_pollution_ville(aqi,
                          co,
                          no,
                          no2,
                          o3,
                          so2,
                          pm2_5,
                          pm10,
                          nh3,
                          day,
                          last_update,
                          id_ville):
    """
    Fonction qui permet d'ajouter un enregistrement dans la table prévision
    :param id_pollution: (nom du champ se suffit à la même)
    :param aqi: (nom du champ se suffit à la même)
    :param co: (nom du champ se suffit à la même)
    :param no: (nom du champ se suffit à la même)
    :param no2: (nom du champ se suffit à la même)
    :param o3: (nom du champ se suffit à la même)
    :param so2: (nom du champ se suffit à la même)
    :param pm2_5: idem
    :param pm_10: (nom du champ se suffit à la même)
    :param nh3: (nom du champ se suffit à la même)
    :param last_update
    """

    sql = """ INSERT INTO pollution ( aqi, co, no, no2, o3, so2, pm2_5, pm10, nh3, day, last_update, id_ville) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

    connection = None
    try:
        # obtention de la connexion à la base de données
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
        # create a new cursor
        cursor = connection.cursor()
        record_to_insert = (aqi, co, no,
                            no2, o3, so2, pm2_5, pm10,
                            nh3, day, date.today(), id_ville)
        cursor.execute(sql, record_to_insert)

        # commit the changes to the database
        connection.commit()
        # close communication with the database
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Erreur ajout_prevision_ville:")
        print(error)
    finally:
        if connection is not None:
            connection.close()


def get_last_update(nom_ville):
    """
    :param nom_ville:
    :return: retourne la date de dernière mise à jour d'une ville dans la table pollution.py
    """
    sql = "select last_update from pollution inner join ville on pollution.id_ville = ville.id_ville where ville.nom = '{0}' limit 1;".format(nom_ville)

    connection = None

    try:
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
        cursor = connection.cursor()
        cursor.execute(sql, nom_ville)
        row = cursor.fetchone()[0]
        connection.commit()
        cursor.close()

        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error get_last_update')
        print(error)
    finally:
        if connection is not None:
            connection.close()



def delete_prevision_ville(nom_ville):
    """
    Supprime les prévisions météo pour une ville
    :param nom_ville: nom de la ville
    :return:
    """
    sql = f"DELETE FROM prevision WHERE id_ville in (select id_ville from ville where nom = '{nom_ville}');"

    connection = None
    try:
        # obtention de la connexion à la base de données
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
        # create a new cursor
        cursor = connection.cursor()

        cursor.execute(sql, nom_ville)

        # commit the changes to the database
        connection.commit()
        # close communication with the database
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Erreur delete_prevision_ville:")
        print(error)
    finally:
        if connection is not None:
            connection.close()


def read_pollution_forecast(ville):
    sql = "select pollution.day,pollution.aqi, pollution.co, pollution.no, pollution.no2, pollution.o3, " \
          "pollution. so2, pollution.pm2_5, pollution.pm10, pollution.nh3 from pollution inner join ville " \
          "on pollution.id_ville = ville.id_ville where ville.nom = '{0}' order by pollution.day;".format(ville)

    connection = None
    try:
        connection = psycopg2.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=PORT)
        cursor = connection.cursor()
        cursor.execute(sql, ville)
        row = cursor.fetchall()
        connection.commit()
        cursor.close()

        return row

    except(Exception, psycopg2.DatabaseError) as error:
        print('Error read_pollution_forecast')
        print(error)
    finally:
        if connection is not None:
            connection.close()


get_id_ville('Dunkerque')