#include <cmath>
#include <cstddef>
#include <cstdlib>
#include <iostream>
#include <ostream>
using namespace std;

void UnsignedDecToBin(int num) {
    cout << "reversed bin = ";
    do {
        cout << (num % 2);
        num /= 2;
    }while (num > 0);
    cout << endl;
}

void SignedDecToBin(int num) {
    int b = ~abs(num) + 1;
    for (int i = 31; i >= 0; i--) {
        cout << ((num >> i) & 1);
    }
    cout << endl;
}

unsigned int binToDec1() {
    int res = 0;
    int a = 0;
    cout << "bin = ";
    while ((a == 0) || (a == 1)) {
        res = res * 2 + a;
        cin >> a;
    }
    return res;
}

unsigned int binToDec2() {
    unsigned int res = 0;
    int a = 0;
    int k = 0;
    cout << "reversed bin = ";
    while ((a == 0) || (a == 1)) {
        res = res + a * (1 << k);
        k++;
        cin >> a;
    }
    return res;
}

int SignedBinToDec() {
    short res{}, a, k{32};
    cout << "bin = ";
    cin >> a;
    while ((a == 1) || (a == 0)) {
        res += a * (1 << k);
        k--;
        cin >> a;
    }
    res = ~(res - 1);
    res = -res;
    return res;
}

unsigned int binToDecShift() {
    unsigned int res = 0;
    int a = 0;
    cout << "bin = ";
    while ((a == 0) || (a == 1)) {
        res = res << 1 | a;
        cin >> a;
    }
    return res;
}

void decToBinShift(int num) {
    cout << "bin = ";
    for (int i = 31; i >= 0; i--) {
        cout << (num & (1 << i));
    }
    cout << endl;
}

int main() {
    int d;
    cout << "decimal = ";
    cin >> d;
    SignedDecToBin(d);
    cout << log2(4294967295) << endl;
    return 0;
}
