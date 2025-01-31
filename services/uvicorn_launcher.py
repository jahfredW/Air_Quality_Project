import os


class Launcher():
    def __init__(self, port):
        """
        Crée un configuration de base pour uvicorn
        utilisation du module os
        :param port: port écouté
        :return : rien du tout
        """
        os.chdir("D:\PycharmProjects\pythonProject4\Air_Quality_Project\services")
        self._project_directory = os.getcwd()
        self._command = f"uvicorn --app-dir {os.getcwd()} bdd_interaction:app --port {str(port)} --reload"
        print(f"Lancement de la commande : {self._command}")
        self._command_launcher()

    def _command_launcher(self):
        os.system(self._command)

class Api_launcher():
    def __init__(self, port):
        os.chdir("D:\PycharmProjects\pythonProject4\Air_Quality_Project\services")
        self._project_directory = os.getcwd()
        print(self._project_directory)
        """
        bin_directory = os.chdir(self._project_directory + "\\venv\\Scripts")
        os.chdir(self._project_directory + "\\services\\")
        print(f"Répertoire de lancement du serveur Web = {bin_directory}")
        """
        print(f"Répertoire du projet = {os.getcwd()}")
        self._command = f"uvicorn --app-dir {os.getcwd()} main_serveur_api:serveur --port {str(port)} --reload"
        print(f"Lancement de la commande : {self._command}")
        self._command_launcher()

    def _command_launcher(self):
        os.system(self._command)

class Vue_launcher():
    def __init__(self):
        os.chdir("D:\\PycharmProjects\\pythonProject4\\Air_Quality_Project\\presentation\\web\\vueJS\\BoldAir")
        self._project_directory = os.getcwd()
        print(self._project_directory)
        print(f"Répertoire du projet = {os.getcwd()}")
        self._command = "npm run dev"
        print(f"Lancement de la commande du serveur Vue JS ")
        self._command_launcher()

    def _command_launcher(self):
        os.system(self._command)

