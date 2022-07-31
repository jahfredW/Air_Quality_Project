import sys
import getopt
from data import meteo_pyowm
from utils import meteo_utils
from services.uvicorn_launcher import Launcher

try:
    opts, argv = getopt.getopt(sys.argv[1:], 'whd:i', ['web','display=', 'interactive', 'help'])

    p = meteo_pyowm.PollutionPyown()

    for opt, argv in opts:
        if opt in ('-d', '--display'):
            print(p.get_prevision_pollution(argv))

        elif opt in ('-h', '--help'):
            print("help")
            meteo_utils.usage()

        elif opt in ('-i, --interactive'):
            ville = input('ville? : Commençant par une majuscule + accents \n')
            liste_villes = p.get_ville(ville)
            print(liste_villes)
            if len(liste_villes) > 1:
                choix = int(input('choix?'))
                try:
                    print("Voici les données brut pour la ville de {}".format(liste_villes[choix]))
                    previsions = p.get_prevision_pollution(liste_villes[choix])
                    for key, value in previsions.items():
                        print(key, value)
                except KeyError as e:
                    print(f'saisie incorrecte : {e}')
                    print(f'Entrez un nombre entre 0 et {len(liste_villes) - 1}')
            else:
                previsions = p.get_prevision_pollution(liste_villes[0])
                for key, value in previsions.items():
                    print(key, value)

        elif opt in ('-w', '--web'):
            print('web')
            l = Launcher()



except getopt.GetoptError:
    print("Paramètres incorrects !")
    sys.exit(2)

