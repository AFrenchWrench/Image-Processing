import numpy as np


def main():
    try:
        i1, j1 = map(int, input().split())
    except:
        print("Cannot be done")
        return
    matrix1 = [list(map(int, input().split())) for _ in range(i1)]
    matrix1 = np.array(matrix1)

    second_line = input().strip()
    tokens = second_line.split()

    if len(tokens) == 1:
        op = tokens[0]
        if op == "scalar":
            try:
                scalar = int(input().strip())
            except:
                print("Cannot be done")
                return
            result = matrix1 * scalar
            for row in result:
                print(" ".join(map(str, row)))
        elif op == "rotate":
            try:
                degree = int(input().strip())
            except:
                print("Cannot be done")
                return
            if degree not in [90, 180, 270]:
                print("Cannot be done")
                return
            else:
                for _ in range(degree // 90):
                    matrix1 = np.rot90(matrix1)
                for row in matrix1:
                    print(" ".join(map(str, row)))
        else:
            print("Cannot be done")
    else:
        try:
            i2, j2 = map(int, tokens)
        except:
            print("Cannot be done")
            return

        matrix2 = [list(map(int, input().split())) for _ in range(i2)]
        matrix2 = np.array(matrix2)

        command = input().strip()

        if command == "add":
            if i1 == i2 and j1 == j2:
                result = matrix1 + matrix2
                for row in result:
                    print(" ".join(map(str, row)))
            else:
                print("Cannot be done")
        elif command == "subtract":
            if i1 == i2 and j1 == j2:
                result = matrix1 - matrix2
                for row in result:
                    print(" ".join(map(str, row)))
            else:
                print("Cannot be done")
        elif command == "multiply":
            if j1 == i2:
                result = np.dot(matrix1, matrix2)
                for row in result:
                    print(" ".join(map(str, row)))
            else:
                print("Cannot be done")
        elif command == "filter":
            if i1 < i2 or j1 < j2:
                print("Cannot be done")
            else:
                out_rows = i1 - i2 + 1
                out_cols = j1 - j2 + 1
                result = np.zeros((out_rows, out_cols), dtype=int)
                for i in range(out_rows):
                    for j in range(out_cols):
                        sub_matrix = matrix1[i : i + i2, j : j + j2]
                        result[i, j] = np.sum(sub_matrix * matrix2)
                for row in result:
                    print(" ".join(map(str, row)))
        else:
            print("Cannot be done")


if __name__ == "__main__":
    main()
