import threading


# Création des threads
def create_threads(list, function):
    threads = []

    for ip in list:
        # On itère sur la listes des adresses IP fournies en paramètres
        # args est un tuple avec un seul élément
        th = threading.Thread(target=function, args=(ip,))
        # Pour chaque IP on crée un thread pour chaque adresse de la liste on utilisant la classe de thread et la
        # méthode start() à partir du module thread pour chaque itération
        th.start()
        # On ajoute les threads à la liste vide qu'on a crée
        threads.append(th)
    # On parcourt la liste des threads, avec la méthode join() on demande au programme d'attendre la fin de
    # tous les threads, afin de pouvoir lire et configurer plusieurs périphériques simultanément.
    for th in threads:
        th.join()
