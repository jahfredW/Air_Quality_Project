import os

# os.system(command)
# on se positionne dans le répertoire bin de l'environnement virtuel python pour démarrer
# le serveur web unicorn
print("Initialisation du serveur...")
project_directory = os.getcwd()
print(project_directory)
bin_directory = os.chdir("D:\\PycharmProjects\\pythonProject4\\Air_Quality_Project\\venv\\Scripts")
print(bin_directory)
print(f"Répertoire du projet = {project_directory}")
print(f"Répertoire de lancement du serveur web = {bin_directory}")
command = f"uvicorn --app-dir {project_directory} bdd_interaction:app --reload"
print(f"Lancement de la commande : {command}")
os.system(command)