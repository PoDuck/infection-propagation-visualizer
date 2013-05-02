from random import randrange
from math import sqrt


class Matrix:

    def __init__(self):
        self._matrix = []
        self._infectedMatrix = []
        self._numPeople = 0
        self._numVaccinated = 0
        self._numInfected = 0
        self._chanceVacInfected = 0.0
        self._chanceUnvacInfected = 0.0
        self._width = 0
        self._primed = False
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def primed(self):
        return self._primed
    
    @primed.setter
    def primed(self, value):
        self._primed = value

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

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value

    @property
    def infectedMatrix(self):
        return self._infectedMatrix

    @infectedMatrix.setter
    def infectedMatrix(self, value):
        self._infectedMatrix = value

    @property
    def numPeople(self):
        return self._numPeople

    @numPeople.setter
    def numPeople(self, numPeople):
        self._numpeople = numPeople

    def checkPosition(self, start, direction):
        x = start[0]
        y = start[1]
        
        if direction == "up":
            if y - 1 < 0:
                y = self.width - 1
            else:
                y -= 1
        elif direction == "down":
            if y + 1 == self.width:
                y = 0
            else:
                y += 1
        elif direction == "left":
            if x - 1 < 0:
                x = self.width - 1
            else:
                x -= 1
        elif direction == "right":
            if x + 1 == self.width:
                x = 0
            else:
                x += 1
        elif direction == "tleft":
            if x - 1 < 0 and y - 1 < 0:
                x = y = self.width - 1
            elif x - 1 < 0:
                x = self.width - 1
                y -= 1
            elif y - 1 < 0:
                y = self.width - 1
                x -= 1
            else:
                x -= 1
                y -= 1
        elif direction == "tright":
            if x + 1 == self.width and y - 1 < 0:
                x = 0
                y = self.width - 1
            elif x + 1 == self.width:
                x = 0
                y -= 1
            elif y - 1 < 0:
                y = self.width - 1
                x -= 1
            else:
                y -= 1
                x += 1
        elif direction == "bleft":
            if x - 1 < 0 and y + 1 == self.width:
                x = self.width - 1
                y = 0
            elif x - 1 < 0:
                x = self.width - 1
                y += 1
            elif y + 1 == self.width:
                y = 0
                x -= 1
            else:
                x -= 1
                y += 1
        elif direction == "bright":
            if x + 1 == self.width and y + 1 == self.width:
                x = y = 0
            elif x + 1 == self.width:
                x = 0
                y += 1
            elif y + 1 == self.width:
                x += 1
                y = 0
            else:
                x += 1
                y += 1
        else:
            return false
        return [x,y]
        

    def checkInfection(self, chance):
        if randrange(0, 1000) <= int(round(chance * 10)):
            return True
        return False

    def vacInfect(self, position):
        if self.checkInfection(self.chanceVacInfected):
            self.infectedMatrix[position[0]][position[1]] = "vacInfected"
            self.infect(position)

    def unvacInfect(self, position):
        if self.checkInfection(self.chanceUnvacInfected):
            self.infectedMatrix[position[0]][position[1]] = "unvacInfected"
            self.infect(position)

    def positionInfect(self, position):
        matrixPos = self.infectedMatrix[position[0]][position[1]]
        if matrixPos == "vacSurvivor":
            self.vacInfect(position)
        elif matrixPos == "unvacSurvivor":
            self.unvacInfect(position)

    def infect(self, position):
        x = position[0]
        y = position[1]
        if (self.infectedMatrix[x][y] == "vacInfected") or (self.infectedMatrix[x][y] == "unvacInfected") or (self.infectedMatrix[x][y] == "infected"):
            directions = ["tleft", "up", "tright", "left", "right", "bleft", "down", "bright"]
            for direction in directions:
                self.positionInfect(self.checkPosition(position, direction))

    def primeMatrix(self, numPeople, numVaccinated, numInfected, chanceVacInfected, chanceUnvacInfected):
        self.matrix = []
        self.infectedMatrix = []
        self.numPeople = numPeople
        self.numVaccinated = numVaccinated
        self.numInfected = numInfected
        self.chanceVacInfected = chanceVacInfected
        self.chanceUnvacInfected = chanceUnvacInfected
        self.width = int(sqrt(self.numPeople))
        
        # initialize matrix (fill with vaccinated people)
        self.matrix = [["vaccinated" for x in range(self.width)] for y in range(self.width)]

        # Set infected people
        count = 0
        while count < self.numInfected:
            x = randrange(0, self.width)
            y = randrange(0, self.width)
            if self.matrix[x][y] == "vaccinated":
                self.matrix[x][y] = "infected"
                count += 1

        # set unvaccinated people
        count = 0
        while count < (self.numPeople - self.numVaccinated - self.numInfected - 1):
            x = randrange(0, self.width)
            y = randrange(0, self.width)
            if self.matrix[x][y] == "vaccinated":
                self.matrix[x][y] = "vaccinated"
                count += 1

        self.primed = True

    def primeInfectedMatrix(self):
        self.infectedMatrix = [["unvacSurvivor" if self.matrix[x][y] != "infected" else "infected" for x in range(self.width)] for y in range(self.width)]

    def propagate(self):
        # Check if primed button has been pressed
        if not self.primed:
            return False

        # reset and prime infected matrix
        self.infectedMatrix = [["unvacSurvivor" if self.matrix[x][y] != "infected" else "infected" for x in range(self.width)] for y in range(self.width)]

        # start infection at all original infection sites
        print "matrix"
        print self.matrix
        for x in range(self.width):
            for y in range(self.width):
                if self.matrix[x][y] == "infected":
                    self.infect([x, y])
        return True


