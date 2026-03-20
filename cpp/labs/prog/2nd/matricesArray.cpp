#include <array>
#include <iomanip>
#include <iostream>

using namespace std;

const int ROWS = 3;
const int COLS = 3;

void outputMatrix(const array<array<int, ROWS>, COLS> &, int, int);
array<array<int, ROWS>, COLS> createMatrix(int, int);
array<array<int, ROWS>, COLS>
sumOrDiffOfMatrixes(const array<array<int, ROWS>, COLS> &,
                    const array<array<int, ROWS>, COLS> &, int, int,
                    int operation = 1);
array<array<int, ROWS>, COLS>
matrixByNumber(const array<array<int, ROWS>, COLS> &, int, int, int);
array<array<int, ROWS>, COLS>
matrixByMatrix(const array<array<int, ROWS>, COLS> &,
               const array<array<int, ROWS>, COLS> &, int, int, int);

int main() {
    array<array<int, ROWS>, COLS> A{5, 1, 7, -10, -2, 1, 0, 1, 2};
    array<array<int, ROWS>, COLS> B{2, 4, 1, 3, 1, 0, 7, 2, 1};
    cout << "Матрица A:\n";
    outputMatrix(A, ROWS, COLS);
    cout << "Матрица B:\n";
    outputMatrix(A, ROWS, COLS);
    array<array<int, ROWS>, COLS> C = matrixByMatrix(
        matrixByNumber(sumOrDiffOfMatrixes(A, B, ROWS, COLS, -1), ROWS, COLS,
                       2),
        sumOrDiffOfMatrixes(matrixByMatrix(A, A, ROWS, COLS, COLS), B, ROWS,
                            COLS),
        ROWS, COLS, COLS);
    cout << "Матрица C:\n";
    outputMatrix(C, ROWS, COLS);

    return 0;
}

array<array<int, ROWS>, COLS> createMatrix(int rows, int cols) {
    array<array<int, ROWS>, COLS> result{};

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << "Введите элемент [" << i + 1 << "][" << j + 1 << "]: ";
            cin >> result[i][j];
        }
    }

    return result;
}

void outputMatrix(const array<array<int, ROWS>, COLS> &mat, int rows,
                  int cols) {
    for (int i = 0; i < rows; i++) {
        cout << "|{ ";
        for (int j = 0; j < cols; j++) {
            cout << setw(4) << mat[i][j];
            if (j != cols - 1)
                cout << ", ";
        }
        cout << " }|\n";
    }
}

array<array<int, ROWS>, COLS>
sumOrDiffOfMatrixes(const array<array<int, ROWS>, COLS> &A,
                    const array<array<int, ROWS>, COLS> &B, int rows, int cols,
                    int operation) {

    array<array<int, ROWS>, COLS> result{};

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            // if (operation == '+')
            //     result[i][j] = A[i][j] + B[i][j];
            // else
            result[i][j] = A[i][j] + operation * B[i][j];
        }
    }

    return result;
}

array<array<int, ROWS>, COLS>
matrixByNumber(const array<array<int, ROWS>, COLS> &A, int rows, int cols,
               int number) {

    array<array<int, ROWS>, COLS> result{};

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            result[i][j] = A[i][j] * number;
        }
    }

    return result;
}

array<array<int, ROWS>, COLS>
matrixByMatrix(const array<array<int, ROWS>, COLS> &A,
               const array<array<int, ROWS>, COLS> &B, int rowsA, int colsA,
               int colsB) {

    array<array<int, ROWS>, COLS> result{};

    for (int i = 0; i < rowsA; i++) {
        for (int j = 0; j < colsB; j++) {
            int sum = 0;
            for (int k = 0; k < colsA; k++) {
                sum += A[i][k] * B[k][j];
            }
            result[i][j] = sum;
        }
    }

    return result;
}
