import sys


# Adresses à ne pas utiliser :
# Loopback: 127.0.0.0/127..255.255.255
# Multicast: 224.0.0.0/239.255.255.255.255
# Broadcast: 255.255.255.255
# Link-Local: 169.254.0.0./169.254.255.255
# Reservé pour utilisation futur: 240.0.0.0/255.255.255.254

# Vérification des octets
def ip_addr_valid(list):
    # On utilise une boucle for pour parcourir la liste des adresses IP
    for ip in list:
        # On supprime les caractères \n à la fin de la chaîne
        ip = ip.rstrip("\n")
        # On divise l'adresse IP en quatre octets on utilisant le point comme délimitateur
        octet_list = ip.split('.')
        # Toutes les conditons doivent être vrai en même temps pour que l'adresse IP soit valide
        if (len(octet_list) == 4) and \
                (1 <= int(octet_list[0]) <= 223) \
                and (int(octet_list[0]) != 127) \
                and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) \
                and (0 <= int(octet_list[1]) <= 255
                     and 0 <= int(octet_list[2]) <= 255
                     and 0 <= int(octet_list[3]) <= 255):
            continue
        else:
            print('\n* L\'adresse IP: {} n\'est pas valide. \n'.format(ip))
            sys.exit()
