#include <iomanip>
#include <iostream>

using namespace std;

void outputArray(int arr[7][7]);
void makeSpiral(int arr[7][7]);
int check(const int arr[7][7], int r, int c);

int main(int argc, char *argv[]) {
    int matr[7][7];
    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++) {
            matr[i][j] = 0;
        }
    }
    makeSpiral(matr);
    outputArray(matr);
    return 0;
}

void outputArray(int arr[7][7]) {
    for (int i = 0; i < 7; i++) {
        cout << "[ ";
        for (int j = 0; j < 7; j++) {
            cout << setw(2) << arr[i][j] << ((j != 6) ? ", " : " ]\n");
        }
    }
}

void makeSpiral(int arr[7][7]) {
    int row = 0;
    int colomn = 0;
    int left = colomn - 1;
    int right = colomn + 1;
    int up = row - 1;
    int down = row + 1;
    int sum = 0;
    int direction = 0;
    for (int i = 0; i <= 49; i++) {
        arr[colomn][row] = i;
        int left = colomn - 1;
        int right = colomn + 1;
        int up = row - 1;
        int down = row + 1;
        sum = check(arr, row, left) + check(arr, row, right) +
              check(arr, up, colomn) + check(arr, down, colomn);
        if (sum >= 3) {
            direction = (direction + 1) % 4;
        }
        switch (direction) {
        case 0:
            row++;
            break;
        case 1:
            colomn++;
            break;
        case 2:
            row--;
            break;
        case 3:
            colomn--;
            break;
        }
    }
}

int check(const int arr[7][7], int r, int c) {
    if ((r < 0) || (r > 6) || (c < 0) || (c > 7))
        return 1;
    return (arr[r][c] != 0) ? 1 : 0;
}
