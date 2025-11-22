#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>

using namespace std;

int getRandom() { return -10 + rand() % 21; }

void outputArray(int arr[3][4]) {
    for (int i = 0; i < 3; i++) {
        cout << "|[";
        for (int j = 0; j < 4; j++) {
            cout << setw(3) << arr[i][j] << ((j != 3) ? ", " : "");
        }
        cout << "]|\n";
    }
}

int main(int argc, char *argv[]) {
    srand(time(nullptr));
    int numbers[3][4];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << "numbers[" << i << "]" << "[" << j << "]  ";
            cin >> numbers[i][j];
        }
    }

    outputArray(numbers);

    int answers[3][4];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            answers[i][j] = 0;
        }
    }
    int min{};
    for (int i = 0; i < 3; i++) {
        min = numbers[0][0];
        for (int j = 0; j < 4; j++) {
            if (numbers[i][j] < min)
                min = numbers[i][j];
        }
        for (int j = 0; j < 4; j++) {
            if (numbers[i][j] == min)
                answers[i][j]++;
        }
    }
    int max{};
    for (int x = 0; x < 4; x++) {
        max = numbers[0][0];
        for (int y = 0; y < 3; y++) {
            if (numbers[y][x] > max)
                max = numbers[y][x];
        }
        for (int y = 0; y < 3; y++) {
            if (numbers[y][x] == max)
                answers[y][x]++;
        }
    }
    bool flag = false;
    cout << "Ответ: ";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            if (answers[i][j] == 2) {
                cout << "A(" << i << "," << j << ") = " << numbers[i][j]
                     << endl;
                flag = true;
            }
        }
    }
    if (!flag)
        cout << "седловых элементов нет\n";
    return 0;
}
