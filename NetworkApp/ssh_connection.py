# Module python pour la gestion des connections à distance via SSH
import paramiko
import os.path
# Module python pour la gestion du temps d'attente pendant que l'execution des commandes
import time
import sys
# Module python pour la recherche des messages d'erreurs que le Routeur pourra générer
import re

# Vérification du fichier nom d'utilisateur/mot de passe
# Inviter l'utilisateur à entrer le nom du fichier contenant utilisateur/mot de passe
user_file = input("\n# Entrez le chemin et le nom du fichier utilisateur: ")

# Vérification de la validité du fichier utilisateur/mot de passe
if os.path.isfile(user_file):
    print("\n* Le fichier nom d'utilisateur/mot de passe est valide.\n")

else:
    print("\n* Le fichier {} n'existe pas. S'il vous plaît, vérifiez et ressayez à nouveau.\n".format(user_file))
    sys.exit()

# Vérification du fichier de commandes
# Inviter l'utilisateur à entrer le nom du fichier contenant les commandes à executer
cmd_file = input("\n# Entrez le chemin et le nom du fichier de commandes: ")

# Vérification de la validité du fichier des commandes
if os.path.isfile(cmd_file):
    print("\n* Le fichier de commande est valide.\n")

else:
    print("\n* Le fichier {} n'existe pas. S'il vous plaît, vérifiez et ressayez à nouveau.\n".format(cmd_file))
    sys.exit()


# Ouverture de la connection SSHv2 vers la machine
def ssh_connection(ip):
    # Utilisation du mot-clé global pour rendre les variables disponibles dans la fonction
    global user_file
    global cmd_file

    # Création d'une connection SSH
    try:
        # Définition des paramètres SSH
        selected_user_file = open(user_file, 'r')

        # Commencer à partir du début du fichier
        selected_user_file.seek(0)

        # Lecture du nom d'utilisateur à partir du fichier
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")

        # Commencer à partir du début du fichier
        selected_user_file.seek(0)

        # Lecture du mot de passe à partir du fichier
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")

        # Connexion à la machine
        session = paramiko.SSHClient()

        # À des fins de test, cela permet d'accepter automatiquement les clés d'hôte inconnues
        # Ne pas utiliser en production! La valeur par défaut serait RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connection à la machine à l'aide du nom d'utilisateur et du mot de passe
        session.connect(ip.rstrip("\n"), username=username, password=password)

        # Démarrez une session shell interactive sur le routeur
        connection = session.invoke_shell()
        connection.send("enable\n")
        # Réglage de la longueur des bornes pour toute la sortie
        # Désactive la pagination
        connection.send("terminal length 0\n")
        time.sleep(1)
        # Entrer en mode de configuration globale
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        # Ouverture du fichier sélectionné par l'utilisateur pour le lire
        selected_cmd_file = open(cmd_file, 'r')

        # Commencer à partir du début du fichier
        selected_cmd_file.seek(0)

        # On parcourt la liste générée par la méthode readlines() appliquée au fichier texte contenant les commandes
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        # Fermeture du fichier utilisateur
        selected_user_file.close()

        # Fermer le fichier de commandes
        selected_cmd_file.close()

        # Vérification de la sortie de commande pour les erreurs de syntaxe IOS
        router_output = connection.recv(65535)
        # Vérification des erreurs générées par le périphérique
        if re.search(b"% Invalid input", router_output):
            print("* Il y a eu au moins une erreur de syntaxe IOS sur l'appareil {}".format(ip))

        else:
            print("\nFAIT pour l'appareil {} :)\n".format(ip))

        # Test de lecture de la sortie de commande
        print(str(router_output) + "\n")

        # Fermeture des connexions
        session.close()

    except paramiko.AuthenticationException:
        print(
            "* Nom d'utilisateur ou mot de passe invalide:( \n* Veuillez vérifier le fichier nom d'utilisateur/mot "
            "de passe ou la configuration de l'appareil.")
        print("* Clôture du programme... Au revoir!")
