# Balance_to_Excel

### Transfert automatiquement la pes�e d'une balance vers un tableur Excel

## Pr�requis
* Windows 7+

## Installation
* Ex�cuter **/Installer/Output/Install_Interface Balances - Excel.exe**

## Utilisation
* Ouvrir le logiciel en mode administrateur
* Connecter la balance au PC via une c�ble s�rie ou avec convertisseur usb/s�rie
* V�rifier le com dans le gestionnaire de p�riph�rique (attention le driver doit �tre install� sur le PC)
* D�clarer une balance en cliquant sur le bouton "Edit config. balance" et renseigner les param�tres* de communication de la balance
* Ouvrir excel en mode administrateur
* A chaque appui sur la touche PRINT de la balance, la donn�e doit s'afficher dans la case du fichier Excel

*Exemple param�tres d'une balance : Com = COM1, Baudrate = 1200, Parity = N (None/Even/Odd), Stopbits = 1, Timeout = 1, Xonxoff = 0, Rtscts = 0

## Programmation
* Python 2.7 - PyQt4 - cx_Freeze pour g�n�rer l'ex�cutable

## Auteur
* **C�dric PERROT** - INRA - (https://github.com/cperrot-inra)

## License
* Gratuit