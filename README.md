![Python 3.6](https://img.shields.io/badge/Python-3.8%2B-green)
![Arista 3.6](https://img.shields.io/badge/Arista-4.20%2B-orange)
![Netmiko 3.0.0](https://img.shields.io/badge/Netmiko-3.3.2-yellow)
![Paramiko 3.0.0](https://img.shields.io/badge/Paramiko-2.7.1-blue)


# Arista-automation

Ce projet est composé de 2 principaux scripts:

- **NETWORKAPP :**
  - Cette application permet d'exécuter automatiquement les commandes contenues dans le fichier cmd.txt sur tous les périphériques Arista connectés via SSH.
  
- **CFGMNGNOTIFICATION :**
    - Ce script permet de surveiller les modifications de configuration sur l'un des commutateurs principeaux du réseau, puis envoyer un e-mail mettant en évidence tous les changements survenus au cours
des dernières 24 heures.

## Prérequis
- Environnement Linux (Testé sous Ubuntu 20.04.1 LTS 64bits)
- Installer Python 3
```
$ sudo apt install python3
```

- Installer le gestionnaire de dépendances de Python3: Pip
```
$ sudo apt install python3-pip
```
- Installer les modules nécessaires au fonctionnement des scripts
```
pip3 install -r requirements.txt
```

## Configuration de l'environnement de test
1 - Présentation de la configuration du réseau:
![](https://zupimages.net/up/20/51/xu66.png)

2 - Installation VirtualBox
- Pour installer la dernière version deVirtualBox, vous devez activer le référentiel 
Multiverse sur votre système. Par défaut, ce référentiel est désactivé.
```
$ sudo add-apt-repository multiverse && sudo apt-get update
```
- Maintenant, entrez la commande suivante pour installer VirtualBox
```
$ sudo apt install virtualbox
```
3 - Installation de 3 VM **Arista EOS** 
- Télécharger les fichiers **vEOS-lab-4.20.15M.vmdk** et **Aboot-veos-8.0.0.iso**:
  https://www.arista.com/en/support/software-download
- Puis les intègrer à VirtualBox

4 - Connexion du PC local aux machines vertuelles Arista sous Linux
- Créer un adaptateur de bouclage afin de se connecter via cet adaptateur à nos machines vertuelles
```
$ sudo su
# apt-get install uml-utilities
# modprobe tun
# tunctl  // Cela créera une interface de bouclage tap0
# ifconfig tap0 10.10.10.100 netmask 255.255.255.0 up
# ip a
```

## Description

Nous avons besoin de 3 fichiers texte, ces trois fichiers sont à configurer **avant l'exécution du script**.

Fichier qui contient les adresses IPs de nos périphériques réseau: **ip.txt**
```bash
10.10.10.2
10.10.10.3
10.10.10.4
```
Fichier qui contient les identifiants utilisés pour ce connecter à chaque switch: **user.txt**
```bash
admin,password
```

Fichier qui contient les commandes que nous voulons exécuter: **cmd.txt** 
```bash
vlan 100
name Management
Vlan 200
name IT
Vlan 300
name RH
ntp server 10.10.10.150
```

## Usage
**1er script:**
```bash
python3 NetworkApp.py
```

**2ème script :**
- Après avoir renseigné les identifiants Gmail executé le script config.py
```bash
python3 config.py
```
## Licence
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


