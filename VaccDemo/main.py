from logic import Matrix

def main():
    output = ""
    matrix = Matrix(36, 25, 5, 15.5, 71.5)
    matrix.propagate()
    for row in matrix.contactMatrix:
        rowout = ""
        for person in row:
            rowout += str(person) + ", "
        output += "[" + rowout[0:-2] + "]\n"
    print output

main()