#include <iomanip>
#include <iostream>

using namespace std;

void outputMatr(int **, int);
int **createMatrix(int);
void populateMatrix(int **, int);
int getRandomInt(int start, int end) {
    return (rand() % (end - start + 1)) + start;
};
int findSum(int **, int);

int main(int argc, char *argv[]) {
    int n;
    do {
        cout << "Введите n: ";
        cin >> n;
    } while (n % 2 == 0);
    int **arr = createMatrix(n);
    outputMatr(arr, n);
    int sum = findSum(arr, n);
    cout << "Найденная сумма: " << sum << endl;
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

void populateMatrix(int **arr, int length) {
    srand(time(nullptr));
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length; j++) {
            arr[i][j] = getRandomInt(-10, 10);
        }
    }
}

int **createMatrix(int n) {
    int **arr = new int *[n];
    for (int i = 0; i < n; i++) {
        arr[i] = new int[n];
    }
    populateMatrix(arr, n);
    return arr;
}

int findSum(int **arr, int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length; j++) {
            if ((i <= j && i + j <= length - 1) ||
                (i >= j && i + j >= length - 1)) {
                cout << arr[i][j] << " ";
                sum += arr[i][j];
            }
        }
        cout << "\n";
    }
    return sum;
}
