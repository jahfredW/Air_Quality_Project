# --------------------------------------------------------------------------- #
#
# script python pour la sauvegarde des tables de la base de données
#
#
# produit un fichier texte (dump)
# Si on renvoit ce fichier au serveur, recrée une base de donnée
# identique à celle sauvegardée
#
#
# --------------------------------------------------------------------------- #
import os
import datetime

if __name__ == '__main__':

    # adapter les valeurs en rapport avec la configuration de votre environnement
    # de développement
    SERVER = "127.0.0.1"
    PORT = 5432
    USER = "dev"
    PASSWORD = "Farte512!"
    SCRIPTS_DIRECTORY = "D:\\PycharmProjects\\pythonProject4\\Air_Quality_Project\\etude\\database\\scripts"
    DATABASE = "test2"
    POSTGRESQL_BIN = "D:\\NEW_DEV\\postgreSQL\\bin"

    SCRIPT_00 = "00_save_database.sql"

    # configuration spécifique pour Windows
    os.chdir(POSTGRESQL_BIN) # on se déplace dans le répertoire des binaires de postgresql (évite de configurer une variable d'environnement sous Windows
    os.environ["PGPASSWORD"] = PASSWORD # définit le mot de passe pour la sessions en cours, car sous Windows, le mot de passe ne peut être soumis via la ligne de commande
    print("Répertoire de travail redéfinit : " + os.getcwd())
    print(os.environ)


    print("Exécution de : '{0}'".format(SCRIPT_00) + " ...")

    command = "pg_dump.exe -U {0} -d {1} -a > {2}\\dump_{3}.txt".format(USER,DATABASE,SCRIPTS_DIRECTORY,datetime.date.today())
    print(command)
    os.system(command)


    print("Fin des traitements.")
