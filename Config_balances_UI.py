# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python\RS232-balances\Config_balances.ui'
#
# Created: Wed Oct 05 22:33:45 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(855, 350)
        Dialog.setMinimumSize(QtCore.QSize(855, 350))
        Dialog.setMaximumSize(QtCore.QSize(855, 350))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Balance.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(357, 325, 151, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.Tab_param = QtGui.QTableWidget(Dialog)
        self.Tab_param.setGeometry(QtCore.QRect(0, 0, 855, 322))
        self.Tab_param.setMinimumSize(QtCore.QSize(855, 322))
        self.Tab_param.setMaximumSize(QtCore.QSize(855, 322))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Tab_param.setFont(font)
        self.Tab_param.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Tab_param.setAutoScroll(False)
        self.Tab_param.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.Tab_param.setDragEnabled(True)
        self.Tab_param.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.Tab_param.setAlternatingRowColors(False)
        self.Tab_param.setShowGrid(True)
        self.Tab_param.setRowCount(100)
        self.Tab_param.setColumnCount(9)
        self.Tab_param.setObjectName(_fromUtf8("Tab_param"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.Tab_param.setHorizontalHeaderItem(8, item)
        self.Tab_param.horizontalHeader().setCascadingSectionResizes(False)
        self.Tab_param.horizontalHeader().setDefaultSectionSize(90)
        self.Tab_param.horizontalHeader().setMinimumSectionSize(90)
        self.Tab_param.horizontalHeader().setSortIndicatorShown(False)
        self.Tab_param.verticalHeader().setDefaultSectionSize(20)
        self.Tab_param.verticalHeader().setMinimumSectionSize(20)
        self.BP_Ouvrir_gest_periph = QtGui.QPushButton(Dialog)
        self.BP_Ouvrir_gest_periph.setGeometry(QtCore.QRect(96, 325, 131, 21))
        self.BP_Ouvrir_gest_periph.setObjectName(_fromUtf8("BP_Ouvrir_gest_periph"))
        self.BP_Suppr_balance = QtGui.QPushButton(Dialog)
        self.BP_Suppr_balance.setGeometry(QtCore.QRect(636, 325, 131, 21))
        self.BP_Suppr_balance.setObjectName(_fromUtf8("BP_Suppr_balance"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Configuration balances", None))
        self.Tab_param.setSortingEnabled(False)
        item = self.Tab_param.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Balance", None))
        item = self.Tab_param.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Port COM", None))
        item = self.Tab_param.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Vitesse", None))
        item = self.Tab_param.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Bits de données", None))
        item = self.Tab_param.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Parité", None))
        item = self.Tab_param.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Bits de stop", None))
        item = self.Tab_param.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Timeout (s)", None))
        item = self.Tab_param.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Xonxoff", None))
        item = self.Tab_param.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Rtscts", None))
        self.BP_Ouvrir_gest_periph.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Ouvrir le gestionnaire de périphériques pour connaître le port COM de la balance</p></body></html>", None))
        self.BP_Ouvrir_gest_periph.setText(_translate("Dialog", "Ouvrir gest. périph.", None))
        self.BP_Suppr_balance.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Sélectrionner la ligne puis supprimer la balance</p></body></html>", None))
        self.BP_Suppr_balance.setText(_translate("Dialog", "Supprimer balance", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

