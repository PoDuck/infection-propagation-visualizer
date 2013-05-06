'''
Created on May 5, 2013

@author: poduck
'''
from random import randrange
from math import sqrt

class Matrix:
    def __init__(self):
        pass

    def prime(self, numPeople, numVaccinated, numInfected, chanceVacInfected, chanceUnvacInfected):
        """
        Initialize all matrices.
        Determines position of initially infected, unvaccinated, and
        healthy people
        """
        self._directions = [[1,1],[0,1],[2,1],[1,0],[2,0],[1,2],[0,2],[2,2]]
        # Number of people in matrix.  Immutable outside prime method.
        self._numPeople = numPeople
        # Number of infected people.  Immutable outside prime method.
        self._numInfected = numInfected
        # Number of vaccinated people.  Immutable outside of prime method.
        self._numVaccinated = numVaccinated
        # Chance a vaccinated person will become infected.
        self._chanceVacInfected = chanceVacInfected
        # Chance an unvaccinated person will become infected.
        self._chanceUnvacInfected = chanceUnvacInfected
        # width of the matrix in number of people.  (All matrices are square.)
        self.cardinalWidth = int(sqrt(numPeople))
        # non-cardinal width.  Starts with 0. 
        self.width = self.cardinalWidth - 1
        
        # fill _matrix with unvaccinated people
        self._matrix = [["unvaccinated" for x in range(self.cardinalWidth)] for y in range(self.cardinalWidth)]

        # set infected people
        count = 0
        while count < self._numInfected:
            x = randrange(0, self.cardinalWidth)
            y = randrange(0, self.cardinalWidth)
            if self._matrix[x][y] == "unvaccinated":
                self._matrix[x][y] = "infected"
                count += 1
        # set vaccinated people
        while count < self._numVaccinated:
            x = randrange(0, self.cardinalWidth)
            y = randrange(0, self.cardinalWidth)
            if self._matrix[x][y] == "unvaccinated":
                self._matrix[x][y] = "vaccinated"
                count += 1

    def checkOverlap(self, direction, position):
        """
        Check if an edge is overlapped.
        if less than zero, the position goes to maximum.
        if greater than maximum, position set to zero.
        returns the new position.
        """
        if direction == 1:
            if position == 0:
                return self.width
            else:
                return (position - 1)
        if direction == 2:
            if position == self.width:
                return 0
            else:
                return (position + 1)
        return position
    
    def changePosition(self, startingPoint, direction):
        """
        Takes in a starting point [x,y] and a direction [x,y] where
        1 = <
        2 = >
        0 = unchanged
        returns the new matrix position.
        """
        (x,y) = startingPoint
        x = self.checkOverlap(direction[0], x)
        y = self.checkOverlap(direction[1], y)
        return [x,y]
    
    def getsInfected(self, status):
        if status == "infected":
            return None
        if status == "vaccinated":
            chance = int(round(self._chanceVacInfected * 10))
        else:
            chance = int(round(self._chanceUnvacInfected * 10))
        if chance > randrange(1, 1001):
            return True
        return False
    
    def spread(self, position):
        for direction in self._directions:
            (x, y) = self.changePosition(position, direction)
            if self.canInfectMatrix[x][y] and not self.contactMatrix[x][y]:
                self.contactMatrix[x][y] = True
                self.spread([x,y])
    
    def propagate(self):
        # initialize canInfectMatrix and contactMatrix
        self.contactMatrix = [[False for row in range(self.cardinalWidth)] for col in range(self.cardinalWidth)]
        self.canInfectMatrix = [[False for row in range(self.cardinalWidth)] for col in range(self.cardinalWidth)]
        for col in range(self.cardinalWidth):
            for row in range(self.cardinalWidth):
                self.canInfectMatrix[row][col] = self.getsInfected(self._matrix[col][row])
        # Spread infection.
        for x in range(self.cardinalWidth):
            for y in range(self.cardinalWidth):
                if self._matrix[x][y] == "infected":
                    self.spread([x,y])
    
    def getFinal(self, position):
        """
        infected = infected
        Vaccinated, immune, contacted = UnvacImmune
        Unvaccinated, immune, contacted = VacImmune
        Vaccinated, not immune, contacted = VacInfected
        Unvaccinated, not immune, contacted = UnvacInfected
        Vaccinated, not immune, not contacted = VacLucky
        unvaccinated, not immune, not contacted = UnvacLucky
        """
        (x, y) = position
        if self._matrix[x][y] == "infected":
            return "infected"
        if self.contactMatrix[x][y]:
            if self.canInfectMatrix[x][y]:
                if self._matrix[x][y] == "vaccinated":
                    return "vacInfected"
                return "unvacInfected"
            if self._matrix[x][y] == "vaccinated":
                return "vacImmune"
            return "unvacImmune"
        if self._matrix[x][y] == "vaccinated":
            return "vacLucky"
        return "unvacLucky"
                    
                    
