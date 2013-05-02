from vacclogic import *


def main():
    matrix = Matrix()
    matrix.primeMatrix(100, 80, 5, 15.1, 75.5)
    if matrix.propagate():
        print list(matrix.infectedMatrix)
    else:
        print "Error"

main()