from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import Logic
import newvacc

class GraphInfect(QDialog, newvacc.Ui_Dialog, Logic.Matrix):
    
    def __init__(self, parent=None):
        super(GraphInfect, self).__init__(parent)
        self.setupUi(self)

        self.primeButton.clicked.connect(self.primePressed)
        self.infectButton.clicked.connect(self.infectPressed)
        self.matrixWidthBox.valueChanged.connect(self.matrixWidthSpinnerChanged)
        self.numInfectedBox.valueChanged.connect(self.infectedSpinnerChanged)
        self.numVaccinatedBox.valueChanged.connect(self.vaccinatedSpinnerChanged)
        self.chanceUnvacInfectedBox.valueChanged.connect(self.updateValues)
        self.chanceVacInfectedBox.valueChanged.connect(self.updateValues)

        self.colors = { "vaccinated":Qt.green, "unvaccinated":Qt.gray, "infected":Qt.red, "vacImmune":Qt.darkGreen, "unvacImmune":Qt.darkGray, "vacInfected":Qt.darkRed, "unvacInfected":Qt.red, "vacLucky":Qt.green, "unvacLucky":Qt.green }
        self.lastPressed = None
        self.matrixWidthSpinnerChanged()

    def primePressed(self):
        self.lastPressed = "prime"
        self.prime()
        self.update()

    def infectPressed(self):
        if not self.lastPressed in ["infect","prime"]:
            QMessageBox.information(self, "Error", "You must prime the matrix first!")
        else:
            self.propagate()
            self.lastPressed = "infect"
            self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setBrush(Qt.white)
        qp.setPen(Qt.transparent)
        if self.lastPressed == "prime":
            self.drawPrimed(qp)
        elif self.lastPressed == "infect":
            self.drawInfected(qp)
        qp.end()

    def prime(self):
        Logic.Matrix.prime(self, self.matrixWidthBox.value()**2, self.numVaccinatedBox.value(), self.numInfectedBox.value(), self.chanceVacInfectedBox.value(), self.chanceUnvacInfectedBox.value())

        self.areaWidth = 435 / self.cardinalWidth
        self.plotStartX = 10
        self.plotStartY = 220
        self.widthX = 561
        self.heightY = 441 
        
        self.startX = self.plotStartX + (self.widthX - (self.areaWidth * self.cardinalWidth))/2
        self.startY = self.plotStartY + (self.heightY - (self.areaWidth * self.cardinalWidth)) / 2
        
        self.update()
        
    def drawPrimed(self, qp):
        qp.setBrush(Qt.white)
        qp.drawRect(self.plotStartX, self.plotStartY, self.widthX, self.heightY)
        for x in range(self.cardinalWidth):
            for y in range(self.cardinalWidth):
                self.plot([x,y], self.colors[self._matrix[x][y]], qp)
    
    def drawInfected(self, qp):
        qp.setBrush(Qt.white)
        qp.drawRect(self.plotStartX, self.plotStartY, self.widthX, self.heightY)
        for x in range(self.cardinalWidth):
            for y in range(self.cardinalWidth):
                self.plot([x,y], self.colors[self.getFinal([x,y])], qp)

    def getPoint(self, position):
        (x, y) = position
        pointX = x * self.areaWidth + self.startX
        pointY = y * self.areaWidth + self.startY
        return [pointX, pointY]

    def plot(self, position, color, qp):
        qp.setBrush(color)
        (x,y) = self.getPoint(position)
        qp.drawRect(x, y, self.areaWidth - 1, self.areaWidth - 1)
    
    def infectedSpinnerChanged(self):
        if self.numInfectedBox.value() + self.numVaccinatedBox.value() > self._numPeople:
            self.numVaccinatedBox.setValue(self._numPeople - self.numInfectedBox.value())
        self.updateValues()
    
    def vaccinatedSpinnerChanged(self):
        if self.numInfectedBox.value() + self.numVaccinatedBox.value() > self._numPeople:
            self.numInfectedBox.setValue(self._numPeople - self.numVaccinatedBox.value())
        self.updateValues()

    def matrixWidthSpinnerChanged(self):
        width = self.matrixWidthBox.value()**2 - 1
        self.numInfectedBox.setMaximum(width)
        self.numVaccinatedBox.setMaximum(width)
        self.updateValues()

    def updateValues(self):
        self._numPeople = self.matrixWidthBox.value() ** 2
        self._numVaccinated = self.numVaccinatedBox.value()
        self._numInfected = self.numInfectedBox.value()
        self._chanceVacInfected = self.chanceVacInfectedBox.value()
        self._chanceUnvacInfected = self.chanceUnvacInfectedBox.value()
        self.showVacNum.setText(str(self._numVaccinated))
        self.showUnvacNum.setText(str(self._numPeople - self._numVaccinated - self._numInfected))
        self.showVacVuln.setText(str(int(round(self._chanceVacInfected / 100 * self._numVaccinated))))
        self.showUnvacVuln.setText(str(int(round(self._chanceUnvacInfected/100 * (self._numPeople - self._numVaccinated - self._numInfected)))))



app = QApplication(sys.argv)
form = GraphInfect()
form.show()
app.exec_()
