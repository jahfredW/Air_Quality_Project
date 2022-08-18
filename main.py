import sys
import getopt
from data import pollution_pyowm
from utils import meteo_utils
from business.components.pollution_ville import PollutionVille
from business.components.pollution import Pollution
from services.uvicorn_launcher import Launcher

try:
    opts, argv = getopt.getopt(sys.argv[1:], 'ahd:iw', ['api', 'display=', 'interactive', 'help', 'web'])



    for opt, argv in opts:
        if opt in ('-d', '--display'):
            p = PollutionVille(argv)
            print(p)

        elif opt in ('-h', '--help'):
            print("help")
            meteo_utils.usage()

        elif opt in ('-i, --interactive'):
            ville = input('ville? : Commençant par une majuscule + accents \n')
            m = pollution_pyowm.PollutionPyown()
            liste_villes = m.get_ville(ville)
            print(liste_villes)
            if len(liste_villes) > 1:
                choix = int(input('choix?'))
                try:
                    print("Voici les données brut pour la ville de {}".format(liste_villes[choix]))
                    p = PollutionVille(liste_villes[choix])
                except KeyError as e:
                    print(f'saisie incorrecte : {e}')
                    print(f'Entrez un nombre entre 0 et {len(liste_villes) - 1}')
            else:
                choix = int(input('choix?'))
                p = PollutionVille(liste_villes[choix])

        elif opt in ('-a', '--api'):
            print('api')
            port = 8050
            l = Launcher(port)

        elif opt in ('-w', '--web'):
            port = 80
            if argv != None and argv != "":
                port = argv



except getopt.GetoptError:
    print("Paramètres incorrects !")
    sys.exit(2)

