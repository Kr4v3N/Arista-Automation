# Importer les modules nécessaires
import sys

from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads

# Enregistrer la liste des adresses IP dans ip.txt dans une variable
ip_list = ip_file_valid()
# Vérification de la validité de chaque adresse IP de la liste
try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print("\n\n* Programme abandonné par l'utilisateur. Quitter...\n")
    sys.exit()
# Vérification de l'accessibilité de chaque adresse IP de la liste
try:
    ip_reach(ip_list)
except KeyboardInterrupt:
    print("\n\n* Programme abandonné par l'utilisateur. Quitter...\n")
    sys.exit()

# Appel de la fonction de création de threads pour une ou plusieurs connexions SSH
create_threads(ip_list, ssh_connection)
