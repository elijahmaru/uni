#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int getRandomInt() { return -50 + rand() % (101); }

void outputArray(int arr[], int length) {
    cout << "[";
    for (int i = 0; i < length; i++) {
        cout << arr[i] << ((i == (length - 1)) ? "" : ", ");
    }
    cout << "]" << endl;
}

void appendArray(int *&arr, int &length, int newValue) {
    int *newArr = new int[length + 1];
    for (int i = 0; i < length; i++) {
        newArr[i] = arr[i];
    }
    newArr[length] = newValue;
    delete[] arr;
    arr = newArr;
    length++;
}

int *firstTask(int[], int);
int *secondTask(int[], int, int);
void thirdTask(int[], int);
pair<int *, int> fourthTask(int[], int);

int main(int argc, char *argv[]) {
    srand(time(nullptr));
    int a[10];
    for (int i = 0; i < 10; i++) {
        a[i] = getRandomInt();
    }
    cout << "Начальный массив: ";
    outputArray(a, 10);
    int x;
    do {
        cout << "Введите X: ";
        cin >> x;
    } while ((x > 9) && (x < 0));
    int z;
    do {
        cout << "Введите Z: ";
        cin >> z;
    } while ((z > 9) && (z < 0));
    int m;
    do {
        cout << "Введите M: ";
        cin >> m;
    } while ((9 - z + 1 - m > 0) && (m > 0));
    int k;
    cout << "Введите K: ";
    cin >> k;
    int y;
    do {
        cout << "Введите Y: ";
        cin >> m;
    } while ((y >= -50) && (y <= 50));
    cout << "1) B: ";
    int *b = firstTask(a, x);
    outputArray(b, 10);
    cout << "2) C: ";
    int *c = secondTask(a, z, m);
    outputArray(c, 10);
    cout << "3) A: ";
    thirdTask(a, k);
    outputArray(a, 10);
    cout << "4) ";
    pair<int *, int> fourthReturn = fourthTask(a, y);
    int fourthLength = fourthReturn.second;
    int *fourthAnswer = new int[fourthLength];
    fourthAnswer = fourthReturn.first;
    outputArray(fourthAnswer, fourthLength);
    return 0;
}

int *firstTask(int arr[], int index) {
    int *newArr = new int[9];
    for (int i = 0, j = 0; i < 9; i++) {
        if (i != index)
            newArr[j++] = arr[i];
    }
    return newArr;
}

int *secondTask(int arr[], int index, int amount) {
    int *newArr = new int[amount];
    memmove(newArr, &arr[index], amount * sizeof(int));
    return newArr;
}

void thirdTask(int arr[], int shift) {
    shift = (10 + shift) % 10;
    int *temp = new int[shift];
    memcpy(temp, arr, shift * sizeof(int));
    memmove(arr, arr + shift, (10 - shift) * sizeof(int));
    memcpy(arr + 10 - shift, temp, shift * sizeof(int));
    delete[] temp;
}

pair<int *, int> fourthTask(int arr[], int number) {
    int length{};
    int *res = new int[1];
    for (int i = 0; i < 10; i++) {
        if (arr[i] == number) {
            appendArray(res, length, number);
        }
    }
    return {res, length};
}
