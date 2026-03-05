#include <iomanip>
#include <iostream>

using namespace std;

void outputMatr(int **, int);
int **createMatrix(int, int, int);
void populateMatrix(int **, int, int, int);
int getRandomInt(int start, int end) {
    return (rand() % (end - start + 1)) + start;
};
void changeNear(int **, int);
void changeQuaters(int **, int);
void mySwap(int *, int *);

int main(int argc, char *argv[]) {
    srand(time(nullptr));
    int n;
    do {
        cout << "Введите n: ";
        cin >> n;
    } while (n % 2 == 1);
    int a = 1;
    int b = 10;
    int **arr = createMatrix(n, a, b);
    cout << "Изначальная матрица :\n";
    outputMatr(arr, n);
    cout << "Изменённая матрица 1 :\n";
    changeNear(arr, n);
    outputMatr(arr, n);

    cout << "Изменённая матрица 2 :\n";
    changeQuaters(arr, n);
    outputMatr(arr, n);
    return 0;
}

void outputMatr(int **arr, int length) {
    for (int i = 0; i < length; i++) {
        cout << "|[";
        for (int j = 0; j < length; j++) {
            cout << setw(4) << arr[i][j] << ((j == length - 1) ? "]|\n" : ", ");
        }
    }
}

void populateMatrix(int **arr, int length, int start, int end) {
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length; j++) {
            arr[i][j] = getRandomInt(start, 10);
        }
    }
}

int **createMatrix(int n, int start, int end) {
    int **arr = new int *[n];
    for (int i = 0; i < n; i++) {
        arr[i] = new int[n];
    }
    populateMatrix(arr, n, start, end);
    return arr;
}

void changeNear(int **arr, int length) {
    for (int i = 0; i < length; i = i + 2) {
        for (int j = 0; j < length; j = j + 2) {
            mySwap(&arr[i][j], &arr[i + 1][j + 1]);
            mySwap(&arr[i][j + 1], &arr[i + 1][j]);
        }
    }
}

void changeQuaters(int **arr, int length) {
    for (size_t i = 0; i < length / 2; i++) {
        for (size_t j = 0; j < length; j++) {
            mySwap(&arr[i][j],
                   &arr[(i + length / 2) % length][(j + length / 2) % length]);
        }
    }
}

void mySwap(int *a, int *b) {
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
}
