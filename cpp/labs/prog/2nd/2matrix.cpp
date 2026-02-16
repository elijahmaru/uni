#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream>
using namespace std;

void outputMatr(int **, int, int);
int **createMatrixMxN(int, int);
void populateMatrixKeyboard(int **, int, int);
void populateMatrix(int **, int, int);
int getRandomInt(int start, int end) {
    return (rand() % (end - start + 1)) + start;
};
int findNumbersFromRangeXY(int **, int, int, int, int);
void formatOrder(int *, int *);

int main(int argc, char *argv[]) {
    srand(time(nullptr));
    int m;
    cout << "Введите m: ";
    cin >> m;
    int n;
    cout << "Введите n: ";
    cin >> n;
    int k;
    cout << "Введите k: ";
    cin >> k;
    int t;
    cout << "Введите t: ";
    cin >> t;
    int **A = createMatrixMxN(m, n);
    int **B = createMatrixMxN(k, t);
    int choice;
    do {
        cout << "Выберете способ заполнения матриц:\n"
                "1) Вводить с клавиатуры\n"
                "2) Заполнить рандомно\n"
                "Выбор: ";
        cin >> choice;
    } while ((choice != 1) && (choice != 2));
    if (choice == 1) {
        cout << "Для матрица A:\n";
        populateMatrixKeyboard(A, m, n);
        cout << "Для матрицы B:\n";
        populateMatrixKeyboard(B, k, t);
    } else {
        populateMatrix(A, m, n);
        populateMatrix(B, k, t);
    }
    cout << "Матрица A:\n";
    outputMatr(A, m, n);
    cout << "Матрица B:\n";
    outputMatr(B, k, t);
    int x, y;
    cout << "Введите x: \n";
    cin >> x;
    cout << "Введите y: \n";
    cin >> y;
    formatOrder(&x, &y);
    int foundInA = findNumbersFromRangeXY(A, m, n, x, y);
    int foundInB = findNumbersFromRangeXY(B, k, t, x, y);
    cout << "Чисел найдено в A: " << foundInA << endl;
    cout << "Чисел найдено в B: " << foundInB << endl;
    return 0;
}

void outputMatr(int **arr, int height, int length) {
    for (int i = 0; i < height; i++) {
        cout << "|[";
        for (int j = 0; j < length; j++) {
            cout << setw(4) << arr[i][j] << ((j == length - 1) ? "]|\n" : ", ");
        }
    }
}

void populateMatrixKeyboard(int **arr, int height, int length) {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < length; j++) {
            cout << "элемент [" << i + 1 << "][" << j + 1 << "]: ";
            cin >> arr[i][j];
        }
    }
}

void populateMatrix(int **arr, int height, int length) {
    int start, end;
    cout << "Введите промежуток из которого будут выбраны рандомные числа\n"
            "Начало отрезка: ";
    cin >> start;
    cout << "Конец отрезка: ";
    cin >> end;
    formatOrder(&start, &end);
    cout << start << ", " << end << endl;
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < length; j++) {
            arr[i][j] = getRandomInt(start, end);
        }
    }
}

int **createMatrixMxN(int amoutOfRows, int amountOfColoms) {
    int **arr = new int *[amoutOfRows];
    for (int i = 0; i < amoutOfRows; i++) {
        arr[i] = new int[amountOfColoms];
    }
    return arr;
}

int findNumbersFromRangeXY(int **arr, int height, int length, int start,
                           int end) {
    int amountFound = 0;
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < length; j++) {
            if (arr[i][j] >= start && arr[i][j] <= end)
                amountFound++;
        }
    }
    return amountFound;
}

void formatOrder(int *a, int *b) {
    if (*a > *b) {
        *a = *a ^ *b;
        *b = *a ^ *b;
        *a = *a ^ *b;
    }
}
