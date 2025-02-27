import sys
from equation_solver import solveEquation
from io_module import getCoefficientInteractive, readCoefficientsFromFile, displayEquation, displayRoots

def main():
    if len(sys.argv) == 1:
        print("")
        a = getCoefficientInteractive("a")
        b = getCoefficientInteractive("b")
        c = getCoefficientInteractive("c")

        displayEquation(a, b, c)
        roots = solveEquation(a, b, c)
        displayRoots(roots)

    elif len(sys.argv) == 2:
        filePath = sys.argv[1]
        try:
            a, b, c = readCoefficientsFromFile(filePath)


            displayEquation(a, b, c)
            roots = solveEquation(a, b, c)
            displayRoots(roots)

        except FileNotFoundError as e:
            print(e)
            sys.exit(1)
        except ValueError as e:
            print(f"{e}")
            sys.exit(1)

    else:
        print("Usage: ./equation <file_path>")
        sys.exit(1)


if __name__ == "__main__":
    main()
