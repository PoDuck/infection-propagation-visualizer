# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newvacc.ui'
#
# Created: Mon May  6 03:06:31 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(585, 674)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 565, 198))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.showUnvacVuln = QtGui.QLabel(self.layoutWidget)
        self.showUnvacVuln.setAccessibleName(_fromUtf8(""))
        self.showUnvacVuln.setObjectName(_fromUtf8("showUnvacVuln"))
        self.gridLayout.addWidget(self.showUnvacVuln, 4, 4, 1, 1)
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setAccessibleName(_fromUtf8(""))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 3)
        self.primeButton = QtGui.QPushButton(self.layoutWidget)
        self.primeButton.setEnabled(True)
        self.primeButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.primeButton.setObjectName(_fromUtf8("primeButton"))
        self.gridLayout.addWidget(self.primeButton, 5, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setAccessibleName(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 2)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setAccessibleName(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 4, 3, 1, 1)
        self.showVacVuln = QtGui.QLabel(self.layoutWidget)
        self.showVacVuln.setAccessibleName(_fromUtf8(""))
        self.showVacVuln.setObjectName(_fromUtf8("showVacVuln"))
        self.gridLayout.addWidget(self.showVacVuln, 3, 4, 1, 1)
        self.infectButton = QtGui.QPushButton(self.layoutWidget)
        self.infectButton.setObjectName(_fromUtf8("infectButton"))
        self.gridLayout.addWidget(self.infectButton, 5, 4, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setAccessibleName(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setAccessibleName(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setAccessibleName(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setAccessibleName(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setAccessibleName(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setAccessibleName(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setAccessibleName(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.numInfectedBox = QtGui.QSpinBox(self.layoutWidget)
        self.numInfectedBox.setAccessibleName(_fromUtf8(""))
        self.numInfectedBox.setMinimum(1)
        self.numInfectedBox.setMaximum(100)
        self.numInfectedBox.setObjectName(_fromUtf8("numInfectedBox"))
        self.gridLayout.addWidget(self.numInfectedBox, 2, 2, 1, 1)
        self.showUnvacNum = QtGui.QLabel(self.layoutWidget)
        self.showUnvacNum.setObjectName(_fromUtf8("showUnvacNum"))
        self.gridLayout.addWidget(self.showUnvacNum, 1, 4, 1, 1)
        self.showVacNum = QtGui.QLabel(self.layoutWidget)
        self.showVacNum.setAccessibleName(_fromUtf8(""))
        self.showVacNum.setObjectName(_fromUtf8("showVacNum"))
        self.gridLayout.addWidget(self.showVacNum, 2, 4, 1, 1)
        self.chanceVacInfectedBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.chanceVacInfectedBox.setDecimals(1)
        self.chanceVacInfectedBox.setSingleStep(0.1)
        self.chanceVacInfectedBox.setObjectName(_fromUtf8("chanceVacInfectedBox"))
        self.gridLayout.addWidget(self.chanceVacInfectedBox, 3, 2, 1, 1)
        self.chanceUnvacInfectedBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.chanceUnvacInfectedBox.setDecimals(1)
        self.chanceUnvacInfectedBox.setSingleStep(0.1)
        self.chanceUnvacInfectedBox.setObjectName(_fromUtf8("chanceUnvacInfectedBox"))
        self.gridLayout.addWidget(self.chanceUnvacInfectedBox, 4, 2, 1, 1)
        self.numVaccinatedBox = QtGui.QSpinBox(self.layoutWidget)
        self.numVaccinatedBox.setAccessibleName(_fromUtf8(""))
        self.numVaccinatedBox.setMaximum(100)
        self.numVaccinatedBox.setObjectName(_fromUtf8("numVaccinatedBox"))
        self.gridLayout.addWidget(self.numVaccinatedBox, 1, 2, 1, 1)
        self.matrixWidthBox = QtGui.QSpinBox(self.layoutWidget)
        self.matrixWidthBox.setMinimum(2)
        self.matrixWidthBox.setMaximum(50)
        self.matrixWidthBox.setProperty("value", 50)
        self.matrixWidthBox.setObjectName(_fromUtf8("matrixWidthBox"))
        self.gridLayout.addWidget(self.matrixWidthBox, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.showNumInfected = QtGui.QLabel(self.layoutWidget)
        self.showNumInfected.setObjectName(_fromUtf8("showNumInfected"))
        self.gridLayout.addWidget(self.showNumInfected, 0, 4, 1, 1)
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 200, 561, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.numVaccinatedBox, self.numInfectedBox)
        Dialog.setTabOrder(self.numInfectedBox, self.chanceVacInfectedBox)
        Dialog.setTabOrder(self.chanceVacInfectedBox, self.chanceUnvacInfectedBox)
        Dialog.setTabOrder(self.chanceUnvacInfectedBox, self.primeButton)
        Dialog.setTabOrder(self.primeButton, self.infectButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Vaccination and Propagation", None, QtGui.QApplication.UnicodeUTF8))
        self.showUnvacVuln.setText(QtGui.QApplication.translate("Dialog", "#uVuln", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "Press prime to setup, infect to see results.", None, QtGui.QApplication.UnicodeUTF8))
        self.primeButton.setText(QtGui.QApplication.translate("Dialog", "Prime", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Chance unvaccinated infected:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Unvaccinated vulnerable:", None, QtGui.QApplication.UnicodeUTF8))
        self.showVacVuln.setText(QtGui.QApplication.translate("Dialog", "#vVuln", None, QtGui.QApplication.UnicodeUTF8))
        self.infectButton.setText(QtGui.QApplication.translate("Dialog", "Infect", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Chance vaccinated infected:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Unvaccinated:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Matrix Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Vaccinated:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "# of people infected:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Vaccinated Vulnerable:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "# of people Vaccinated:", None, QtGui.QApplication.UnicodeUTF8))
        self.showUnvacNum.setText(QtGui.QApplication.translate("Dialog", "#UnVac", None, QtGui.QApplication.UnicodeUTF8))
        self.showVacNum.setText(QtGui.QApplication.translate("Dialog", "#Vac", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Final Number Infected:", None, QtGui.QApplication.UnicodeUTF8))
        self.showNumInfected.setText(QtGui.QApplication.translate("Dialog", "Null", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

