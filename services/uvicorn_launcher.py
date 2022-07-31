import os


class Launcher():
    def __init__(self):
        self.project_directory = os.getcwd()
        self.bin_directory = os.chdir(self.project_directory + '\\services\\routers\\')
        print(f"Répertoire du projet = {self.bin_directory}")
        self.command = f"uvicorn --app-dir {self.project_directory} bdd_interaction:app --reload"
        print(f"Lancement de la commande : {self.command}")
        self._command_launcher()

    def _command_launcher(self):
        os.system(self.command)
    # os.system(command)
# on se positionne dans le répertoire bin de l'environnement virtuel python pour démarrer
# le serveur web unicorn

"""
print("Initialisation du serveur...")
        
print(project_directory)
bin_directory = os.chdir("D:\\PycharmProjects\\pythonProject4\\Air_Quality_Project\\venv\\Scripts")
print(bin_directory)
print(f"Répertoire du projet = {project_directory}")
print(f"Répertoire de lancement du serveur web = {bin_directory}")
os.system(command)
"""