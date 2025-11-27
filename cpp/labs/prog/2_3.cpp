#include <cstdlib>
#include <cstring>
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

float avgOfPosOdd(int[], int);

int main (int argc, char *argv[]) {
    srand(time(nullptr));
    int m;
    cout << "Введите M: " << endl;
    cin >> m;
    int x[m];
    int z[m];
    for (int i = 0; i < m; i++) {
        x[i] = getRandomInt();
        z[i] = getRandomInt();
    }
    float answerForX;
    float answerForZ;
    return 0;
}

float avgOfPosOdd(int arr[], int length){
    float avg{.0};
    int count{};
    for (int i = 0; i < length; i++) {
        if ((arr[i] % 2 == 1) && (arr[i] > 0)) {
            avg += arr[i];
            count++;
        }
    }
    return avg/count;
}
