#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int main() {
    string binary;
    int decimal;
    char sign{};
    cout << "1. Введите десятичное число: ";
    cin >> decimal;
    if (decimal < 0) {
        sign = '-';
        decimal = abs(decimal);
    }
    do {
        binary = to_string(decimal % 2) + binary;
        decimal /= 2;
    } while (decimal > 0);
    binary = sign + binary;
    cout << binary << endl;

    string hex;
    cout << "2. Введите десятичное число: ";
    cin >> decimal;
    string last;
    if (decimal < 0) {
        sign = '-';
        decimal = abs(decimal);
    }
    while (decimal > 0) {
        if (decimal % 16 >= 10) {
            last = (char)(decimal % 16 + 55);
        } else {
            last = to_string(decimal % 16);
        }
        hex = last + hex;
        decimal /= 16;
    }
    hex = sign + hex;
    cout << hex << endl;
}
