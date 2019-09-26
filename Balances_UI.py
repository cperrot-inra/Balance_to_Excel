# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\RS232-balances\Balances.ui'
#
# Created: Wed Oct 05 22:33:44 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(290, 115)
        MainWindow.setMinimumSize(QtCore.QSize(290, 115))
        MainWindow.setMaximumSize(QtCore.QSize(290, 115))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Balance.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.comboBox_deplacement = QtGui.QComboBox(self.centralwidget)
        self.comboBox_deplacement.setGeometry(QtCore.QRect(150, 14, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_deplacement.setFont(font)
        self.comboBox_deplacement.setStyleSheet(_fromUtf8(""))
        self.comboBox_deplacement.setIconSize(QtCore.QSize(16, 16))
        self.comboBox_deplacement.setModelColumn(0)
        self.comboBox_deplacement.setObjectName(_fromUtf8("comboBox_deplacement"))
        self.comboBox_deplacement.addItem(_fromUtf8(""))
        self.comboBox_deplacement.addItem(_fromUtf8(""))
        self.comboBox_deplacement.addItem(_fromUtf8(""))
        self.comboBox_deplacement.addItem(_fromUtf8(""))
        self.comboBox_balances = QtGui.QComboBox(self.centralwidget)
        self.comboBox_balances.setGeometry(QtCore.QRect(10, 14, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_balances.setFont(font)
        self.comboBox_balances.setStyleSheet(_fromUtf8(""))
        self.comboBox_balances.setIconSize(QtCore.QSize(16, 16))
        self.comboBox_balances.setObjectName(_fromUtf8("comboBox_balances"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 0, 121, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(8)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 0, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BP_Edit_fichier_config = QtGui.QPushButton(self.centralwidget)
        self.BP_Edit_fichier_config.setGeometry(QtCore.QRect(80, 88, 131, 21))
        font = QtGui.QFont()
        font.setItalic(False)
        self.BP_Edit_fichier_config.setFont(font)
        self.BP_Edit_fichier_config.setObjectName(_fromUtf8("BP_Edit_fichier_config"))
        self.Affich_log = QtGui.QLabel(self.centralwidget)
        self.Affich_log.setGeometry(QtCore.QRect(10, 60, 271, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Affich_log.setFont(font)
        self.Affich_log.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.Affich_log.setText(_fromUtf8(""))
        self.Affich_log.setAlignment(QtCore.Qt.AlignCenter)
        self.Affich_log.setObjectName(_fromUtf8("Affich_log"))
        self.Save_continu = QtGui.QCheckBox(self.centralwidget)
        self.Save_continu.setGeometry(QtCore.QRect(16, 32, 131, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.Save_continu.setFont(font)
        self.Save_continu.setChecked(True)
        self.Save_continu.setTristate(False)
        self.Save_continu.setObjectName(_fromUtf8("Save_continu"))
        self.Del_cell = QtGui.QCheckBox(self.centralwidget)
        self.Del_cell.setGeometry(QtCore.QRect(155, 32, 131, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.Del_cell.setFont(font)
        self.Del_cell.setChecked(False)
        self.Del_cell.setTristate(False)
        self.Del_cell.setObjectName(_fromUtf8("Del_cell"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox_balances, self.comboBox_deplacement)
        MainWindow.setTabOrder(self.comboBox_deplacement, self.Save_continu)
        MainWindow.setTabOrder(self.Save_continu, self.Del_cell)
        MainWindow.setTabOrder(self.Del_cell, self.BP_Edit_fichier_config)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Interface Balances - Excel", None))
        self.comboBox_deplacement.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Sélectionner le sens de déplacement dans le tableau Excel</p></body></html>", None))
        self.comboBox_deplacement.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.comboBox_deplacement.setItemText(0, _translate("MainWindow", "Bas", None))
        self.comboBox_deplacement.setItemText(1, _translate("MainWindow", "Haut", None))
        self.comboBox_deplacement.setItemText(2, _translate("MainWindow", "Droite", None))
        self.comboBox_deplacement.setItemText(3, _translate("MainWindow", "Gauche", None))
        self.comboBox_balances.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Sélectionner la balance</p></body></html>", None))
        self.comboBox_balances.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Balance</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Sens déplacement Excel</p></body></html>", None))
        self.BP_Edit_fichier_config.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Ajouter / modifier / supprimer les paramètres d\'une balance</p></body></html>", None))
        self.BP_Edit_fichier_config.setText(_translate("MainWindow", "Editer config. balances", None))
        self.Affich_log.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Boîte de dialogue</p></body></html>", None))
        self.Save_continu.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Enregistrement automatique du fichier Excel après chaque acquisition</p></body></html>", None))
        self.Save_continu.setText(_translate("MainWindow", "Enregistrement auto.", None))
        self.Del_cell.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Forcer l\'écriture quel que soit le contenu de la cellule du tableau Excel</p></body></html>", None))
        self.Del_cell.setText(_translate("MainWindow", "Forcer écriture cellule", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

