from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import vaccdemo
from vacclogic import Matrix


class MainDialog(QDialog, vaccdemo.Ui_Dialog):

    def __init__(self, parent=None):

        self._numPeople = 100
        self._numVaccinated = 0
        self._numInfected = 1
        self._numUnvaccinated = 0
        self._chanceVacInfected = 0
        self._chanceUnvacInfected = 0
        self._vaccVulnerable = 0
        self._unvacVulnerable = 0
        self._matrix = Matrix()
        self.primePressed = False
        self.infectPressed = False

        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.numInfectedBox.setMinimum(1)
        self.showVacNum.setText(str(self.numVaccinatedBox.value()))
        self.recalcValues()
        self.showUnvacNum.setText(str(int(self.numPeopleCombo.currentText()) - self.numVaccinatedBox.value()))
        self.numInfectedBox.setMaximum(self.numPeople - 1)
        self.connect(self.infectButton, SIGNAL("clicked()"), self.calculate)
        self.connect(self.primeButton, SIGNAL("clicked()"), self.prime)
        self.connect(self.numPeopleCombo, SIGNAL("currentIndexChanged(int)"), self.recalcValues)
        self.connect(self.numInfectedBox, SIGNAL("valueChanged(int)"), self.recalcValues)
        self.connect(self.numVaccinatedBox, SIGNAL("valueChanged(int)"), self.recalcValues)
        self.connect(self.chanceVacInfectedBox, SIGNAL("valueChanged(int)"), self.recalcValues)
        self.connect(self.chanceUnvacInfectedBox, SIGNAL("valueChanged(double)"), self.recalcValues)

    @property
    def unvacVulnerable(self):
        return self._unvacVulnerable

    @unvacVulnerable.setter
    def unvacVulnerable(self, value):
        self._unvacVulnerable = value
        self.showUnvacVuln.setText("~" + str(value))

    @property
    def vaccVulnerable(self):
        return self._vaccVulnerable

    @vaccVulnerable.setter
    def vaccVulnerable(self, value):
        self._vaccVulnerable = value
        self.showVacVuln.setText("~" + str(value))

    @property
    def chanceUnvacInfected(self):
        return self._chanceUnvacInfected

    @chanceUnvacInfected.setter
    def chanceUnvacInfected(self, value):
        self._chanceUnvacInfected = value

    @property
    def chanceVacInfected(self):
        return self._chanceVacInfected

    @chanceVacInfected.setter
    def chanceVacInfected(self, value):
        self._chanceVacInfected = value

    @property
    def numUnvaccinated(self):
        return self._numUnvaccinated

    @numUnvaccinated.setter
    def numUnvaccinated(self, value):
        self._numUnvaccinated = value
        self.showUnvacNum.setText(str(value))

    @property
    def numInfected(self):
        return self._numInfected

    @numInfected.setter
    def numInfected(self, value):
        self._numInfected = value

    @property
    def numVaccinated(self):
        return self._numVaccinated

    @numVaccinated.setter
    def numVaccinated(self, value):
        self._numVaccinated = value
        self.showVacNum.setText(str(value))

    @property
    def numPeople(self):
        return self._numPeople

    @numPeople.setter
    def numPeople(self, value):
        self._numPeople = value
    
    @property
    def matrix(self):
        return self._matrix
    
    @matrix.setter
    def matrix(self, value):
        self._matrix = value

    def recalcValues(self):
        self.numPeople = int(self.numPeopleCombo.currentText())
        self.numVaccinated = self.numVaccinatedBox.value()
        self.numInfected = self.numInfectedBox.value()
        self.chanceVacInfected = self.chanceVacInfectedBox.value()
        self.chanceUnvacInfected = self.chanceUnvacInfectedBox.value()
        self.numUnvaccinated = self.numPeople - self.numVaccinated
        self.vaccVulnerable = int(round(self.chanceVacInfected/100 * self.numVaccinated))
        self.unvacVulnerable = int(round(self.chanceUnvacInfected/100 * (self.numPeople - self.numVaccinated - self.numInfected)))
        self.numVaccinatedBox.setMaximum(self.numPeople)
        self.numInfectedBox.setMaximum(self.numPeople - 1)
        self.numUnvaccinated = self.numPeople - self.numVaccinated - self.numInfected
        if self.numPeople - self.numInfected < self.numVaccinated:
            self.numVaccinatedBox.setValue(self.numPeople - self.numInfected)
        if self.numPeople - self.numVaccinated < self.numInfected:
            self.numInfectedBox.setValue(self.numPeople - self.numVaccinated)
        self.numVaccinated = self.numVaccinatedBox.value()
    
    def drawCircles(self,qp):
        if self.primePressed or self.infectPressed:
            sqWidth = 435 / self.matrix.width
            diameter = sqWidth - 2
            startY = 220 + (441 - (sqWidth * self.matrix.width)) / 2
            startX = 10 + (561 - (sqWidth * self.matrix.width)) / 2
            position = [startX, startY]
            if self.primePressed:
                matrix = self.matrix.matrix
            elif self.infectPressed:
                matrix = self.matrix.infectedMatrix
            for row in matrix:
                for person in row:
                    if person == "infected":
                        qp.setBrush(Qt.red)
                    elif person == "vaccinated":
                        qp.setBrush(Qt.green)
                    elif person == "unvaccinated":
                        qp.setBrush(Qt.gray)
                    elif person == "vacInfected":
                        qp.setBrush(Qt.darkMagenta)
                    elif person == "unvacInfected":
                        qp.setBrush(Qt.yellow)
                    elif person == "vacSurvivor":
                        qp.setBrush(Qt.darkGray)
                    elif person == "unvacSurvivor":
                        qp.setBrush(Qt.darkGreen)
                    qp.drawRect(position[0],position[1],diameter,diameter)
                    position[0] += sqWidth
                position[0] = startX
                position[1] += sqWidth

    def prime(self):
        self.matrix.primeMatrix(self.numPeople, self.numVaccinated, self.numInfected, self.chanceVacInfected, self.chanceUnvacInfected)
        self.primePressed = True
        self.infectPressed = False
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        # qp.setRenderHint(QPainter.Antialiasing)
        qp.setBrush(Qt.white)
        qp.setPen(Qt.transparent)
        qp.drawRect(10,220,560,440)
        self.drawCircles(qp)
        qp.end()

    def calculate(self):
        if self.matrix.propagate():
            self.infectPressed = True
            self.primePressed = False
            self.update()
        else:
            QMessageBox.about(self, "Error", "You must prime the matrix first!")

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()


