# Importation des modules nécessaires
import difflib
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from netmiko import ConnectHandler


# Définition de l'appareil à surveiller
ip = '10.10.10.3'

# Définition du type d'appareil pour l'exécution de netmiko
device_type = 'arista_eos'

# Définition du nom d'utilisateur et du mot de passe pour exécuter netmiko
username = 'admin'
password = 'password'

# Définition de la commande à envoyer à chaque appareil
command = 'show running'


# Connexion à l'appareil via SSH
session = ConnectHandler(device_type=device_type, ip=ip, username=username, password=password,
                         global_delay_factor=3)

# Entrer en mode d'activation
enable = session.enable()

# Envoi de la commande et stockage de la sortie (configuration en cours)
output = session.send_command(command)

# Définition du fichier d'hier, pour comparaison
device_cfg_old = 'cfgfiles/' + ip + '_' + \
    (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

# Écriture de la sortie de la commande dans un fichier pour aujourd'hui
with open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'w') as device_cfg_new:
    device_cfg_new.write(output + '\n')


# Extraire les différences entre les fichiers d'hier et d'aujourd'hui au format HTML
with open(device_cfg_old, 'r') as old_file, \
        open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'r') as new_file:
    difference = difflib.HtmlDiff().make_file(fromlines=old_file.readlines(
    ), tolines=new_file.readlines(), fromdesc='Hier', todesc="Aujourd'hui")


# Envoi des différences par e-mail
#
# Définition des paramètres de messagerie
fromaddr = 'test@gmail.com'
toaddr = 'test@gmail.com'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Rapport de gestion de la configuration quotidienne'
msg.attach(MIMEText(difference, 'html'))

# Envoi de l'e-mail via le serveur SMTP de Gmail sur le port 587
server = smtplib.SMTP('smtp.gmail.com', 587)

# La connexion SMTP est en mode TLS (Transport Layer Security). Toutes les commandes SMTP qui suivent seront cryptées.
server.starttls()

# Connexion à Gmail et envoi de l'e-mail
server.login('myid', 'mypassword')
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()



