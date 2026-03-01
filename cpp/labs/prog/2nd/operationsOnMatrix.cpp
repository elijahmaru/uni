#include <iostream>
#include <vector>

using namespace std;

void outputMatrix(vector<vector<int>> &);
vector<vector<int>> createMatrix();
vector<vector<int>> sumOrDiffOfMatrixes(vector<vector<int>> &,
                                        vector<vector<int>> &, char);
vector<vector<int>> matrixByNumber(vector<vector<int>> &, int);
vector<vector<int>> matrixByMatrix(vector<vector<int>> &,
                                   vector<vector<int>> &);

int main(int argc, char *argv[]) {
    vector<vector<int>> A = createMatrix();
    vector<vector<int>> B = createMatrix();
    vector<vector<int>> C = matrixByMatrix(A, A);
    C = sumOrDiffOfMatrixes(C, B, '+');
    vector<vector<int>> buff = sumOrDiffOfMatrixes(A, B, '-');
    buff = matrixByNumber(buff, 2);
    C = matrixByMatrix(buff, C);
    outputMatrix(C);
    /*if (A.size() == B.size() && A[0].size() == B[0].size()) {
        char operation = '=';
        do {
            cout << "Введите какую операцию вы хотите совешить(+/-): ";
            cin >> operation;
        } while (operation != '+' && operation != '-');
        C = sumOrDiffOfMatrixes(A, B, operation);
        outputMatrix(C);
    } else {
        cout << "Матрицы нельзя сложить";
    }
    int scalar;
    cout << "На какое число хотите умножить матрицы: ";
    cin >> scalar;
    C = matrixByNumber(A, scalar);
    outputMatrix(C);
    C = matrixByNumber(B, scalar);
    outputMatrix(C);
    if (A[0].size() == B.size()) {
        C = matrixByMatrix(A, B);
        outputMatrix(C);
    } else {
        cout << "Матрицы нельзя умножить";
    }*/
    return 0;
}

vector<vector<int>> createMatrix() {
    vector<vector<int>> resultVector;
    int m;
    cout << "Введите кол-во столбцов: ";
    cin >> m;
    int n;
    cout << "Введите кол-во строк: ";
    cin >> n;
    for (int i = 0; i < m; i++) {
        vector<int> row(n);
        for (int j = 0; j < n; j++) {
            cout << "Введеите елемент [" << (i + 1) << "][" << (j + 1) << "]: ";
            cin >> row[j];
        }
        resultVector.push_back(row);
    }
    return resultVector;
}

void outputMatrix(vector<vector<int>> &vec) {
    for (vector<vector<int>>::iterator iteratorOfRows = vec.begin();
         iteratorOfRows != vec.end(); ++iteratorOfRows) {
        cout << "|{ ";
        for (vector<int>::iterator iter = iteratorOfRows->begin();
             iter != iteratorOfRows->end(); ++iter) {
            cout << *iter
                 << ((iter != iteratorOfRows->end() - 1) ? ", " : "}|\n");
        }
    }
}

vector<vector<int>> sumOrDiffOfMatrixes(vector<vector<int>> &A,
                                        vector<vector<int>> &B,
                                        char operation) {

    int rows = A.size();
    int coloms = A[0].size();
    vector<vector<int>> resultVector(rows, vector<int>(coloms));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < coloms; j++) {
            resultVector[i][j] =
                (operation == '+') ? A[i][j] + B[i][j] : A[i][j] - B[i][j];
        }
    }
    return resultVector;
}

vector<vector<int>> matrixByNumber(vector<vector<int>> &A, int number) {
    vector<vector<int>> resultVector(A.size(), vector<int>(A[0].size()));
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < A[0].size(); j++) {
            resultVector[i][j] = A[i][j] * number;
        }
    }
    return resultVector;
}

vector<vector<int>> matrixByMatrix(vector<vector<int>> &A,
                                   vector<vector<int>> &B) {

    vector<vector<int>> resultVector(A.size(), vector<int>(B[0].size()));
    for (int i = 0; i < resultVector.size(); i++) {
        for (int j = 0; j < resultVector[0].size(); j++) {
            int sum = 0;
            for (int k = 0; k < A[0].size(); k++) {
                sum += A[i][k] * B[k][j];
            }
            resultVector[i][j] = sum;
        }
    }
    return resultVector;
}
