# Balance_to_Excel

### Transfert automatiquement la pesée d'une balance vers un tableur Excel

## Prérequis
* Windows 7+

## Installation
* Exécuter **/Installer/Output/Install_Interface Balances - Excel.exe**

## Utilisation
* Ouvrir le logiciel en mode administrateur
* Connecter la balance au PC via une câble série ou avec convertisseur usb/série
* Vérifier le com dans le gestionnaire de périphérique (attention le driver doit être installé sur le PC)
* Déclarer une balance en cliquant sur le bouton "Edit config. balance" et renseigner les paramètres* de communication de la balance
* Ouvrir excel en mode administrateur
* A chaque appui sur la touche PRINT de la balance, la donnée doit s'afficher dans la case du fichier Excel

*Exemple paramètres d'une balance : Com = COM1, Baudrate = 1200, Parity = N (None/Even/Odd), Stopbits = 1, Timeout = 1, Xonxoff = 0, Rtscts = 0

## Programmation
* Python 2.7 - PyQt4 - cx_Freeze pour générer l'exécutable

## Auteur
* **Cédric PERROT** - INRA - (https://github.com/cperrot-inra)

## License
* Gratuit