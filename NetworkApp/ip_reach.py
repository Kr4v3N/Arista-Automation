import sys
# Utilisation du module subprocess pour effectuer le ping sur chaque périférique
import subprocess


# Vérification de l'accessibilité de l'adresse IP
def ip_reach(list):
    for ip in list:
        # On supprime les caractères \n à la fin de la chaîne
        ip = ip.rstrip("\n")
        ping_reply = subprocess.call('ping %s -c 2' % ip, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                     shell=True)
        if ping_reply == 0:
            print("\n* {} est joignable.\n".format(ip))
            continue
        else:
            print('\n* {} n\'est pas joignable. Vérifiez la connectivité et réessayez.'.format(ip))
            sys.exit()
