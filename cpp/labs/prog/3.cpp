#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int getRandomInt() { return -50 + rand() % (101); }
int countPosUneven(int *&arr, int length);
void outputArray(int *&arr, int length);

int main(int argc, char *argv[]) {
    srand(time(nullptr));
    int length;
    cout << "Введите длину массивов n: ";
    cin >> length;
    int *X = new int[length];
    int *Y = new int[length];
    for (int i = 0; i < length; i++) {
        X[i] = getRandomInt();
        Y[i] = getRandomInt();
    }
    cout << "Массив X: ";
    outputArray(X, length);
    cout << "Массив Y: ";
    outputArray(Y, length);
    cout << "Кол-во нечетных элементов в массиве X: "
         << countPosUneven(X, length) << endl;
    cout << "Кол-во нечетных элементов в массиве X: "
         << countPosUneven(X, length) << endl;
    return 0;
}

void outputArray(int *&arr, int length) {
    cout << "[ ";
    for (int i = 0; i < length; i++) {
        cout << arr[i] << ((i != (length - 1)) ? ", " : " ]\n");
    }
}

int countPosUneven(int *&arr, int length) {
    int sum{};
    for (int i = 0; i < length; i++) {
        int item = arr[i];
        if ((item > 0) & (item % 2 == 1))
            sum += item;
    }
    return sum;
}
