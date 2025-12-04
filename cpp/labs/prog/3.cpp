#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

void createArr(int *&arr, int length);
int getRandomInt(int start = 0, int end = 100) {
    return start + rand() % (end - start + 1);
}
int countPositiveUneven(int *arr, int length);
void outputArray(int *arr, int length);

int main(int argc, char *argv[]) {
    srand(time(nullptr));
    cout << "Задание (a) :" << endl;
    int length;
    cout << "Введите длину массивов n: ";
    cin >> length;
    int length1;
    cout << "Введите длину массивов m: ";
    cin >> length1;
    int *X;
    int *Y;
    createArr(X, length);
    createArr(Y, length1);
    cout << "Массив X: ";
    outputArray(X, length);
    cout << "Массив Y: ";
    outputArray(Y, length1);
    cout << "Кол-во нечетных элементов в массиве X: "
         << countPositiveUneven(X, length) << endl;
    cout << "Кол-во нечетных элементов в массиве Y: "
         << countPositiveUneven(Y, length1) << endl;
    return 0;
}

void createArr(int *&arr, int length) {
    arr = new int[length];
    for (int i = 0; i < length; i++) {
        arr[i] = getRandomInt(-100, 100);
    }
}

void outputArray(int *arr, int length) {
    cout << "[ ";
    for (int i = 0; i < length; i++) {
        cout << arr[i] << ((i != (length - 1)) ? ", " : " ]\n");
    }
}

int countPositiveUneven(int *arr, int length) {
    int sum{};
    for (int i = 0; i < length; i++) {
        int item = arr[i];
        if ((item > 0) & (item % 2 == 1))
            sum += item;
    }
    return sum;
}
