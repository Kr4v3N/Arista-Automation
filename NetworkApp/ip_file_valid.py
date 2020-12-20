# Importations des modules nécessaire au fonctionnement du script

import os.path
import sys


# Vérification si le fichier d'adresses IP spécifié par l'utilisateur est bien présent sur le système de fichiers local.
def ip_file_valid():
    # Demander à l'utilisateur de saisir le nom et le chemin d'accès complet du fichier
    ip_file = input("\n# Renseignez le nom et le chemin d'accès au fichier contenant les adresses IP: ")
    # Vérifier si le fichier existe
    if os.path.isfile(ip_file):
        print("\n* Le fichier d'adresses IP est valide. \n")
    else:
        print("\n* Le fichier {} n'existe pas. S'il vous plaît, vérifiez et ressayez à nouveau.\n".format(ip_file))
        sys.exit()
    # Ouvrir le fichier sélectionné par l'utilisateur pour la lecture (fichier d'adresses IP)
    selected_ip_file = open(ip_file, 'r')
    # Commnecer à partir du début du fichier
    selected_ip_file.seek(0)
    # Lecture de chaque ligne (adresse IP) du fichier
    ip_list = selected_ip_file.readlines()
    # Fermeture du fichier
    selected_ip_file.close()
    # Renvoie la listes des adresses IP
    return ip_list
