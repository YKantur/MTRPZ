import math
import sys

def getCoefficientInteractive(coefficientName):
    while True:
        try:
            valueStr = input(f"{coefficientName} = ")
            value = float(valueStr)
            return value
        except ValueError:
            print(f"Error. Expected a valid real number, got {valueStr} instead")

def readCoefficientsFromFile(filePath):
    try:
        with open(filePath, 'r') as f:
            fileContent = f.read()

            lines = fileContent.splitlines() # Split by newlines

            if len(lines) != 1:
                raise ValueError("invalid file format")

            coefficientLine = lines[0]
            coeffsStr = coefficientLine.split(' ')


            if len(coeffsStr) != 3:
                raise ValueError("invalid file format")

            try:
                a, b, c = map(float, coeffsStr)
            except ValueError:
                raise ValueError("invalid file format")

            if a == 0.0:
                raise ValueError("Error. a cannot be 0")

            expectedContent = f"{coeffsStr[0]} {coeffsStr[1]} {coeffsStr[2]}"
            if coefficientLine != expectedContent:
                raise ValueError("invalid file format")

            if not fileContent.endswith('\n'):
                 raise ValueError("invalid file format")

            return (a, b, c)

    except FileNotFoundError:
        raise FileNotFoundError(f"file {filePath} does not exist")

def displayEquation(a, b, c):
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

def displayRoots(roots):
    numRoots = len(roots)
    print(f"There are {numRoots} roots")
    if numRoots >= 1:
        print(f"x1 = {roots[0]}")
    if numRoots == 2:
        print(f"x2 = {roots[1]}")
