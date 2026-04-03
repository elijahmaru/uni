#include <iostream>
#include <stdexcept>
using namespace std;

int fractalOfWhatNumber(int);
int factorial(int);

int main(int argc, char *argv[]) {
    int number;
    cout << "Введите число: ";
    cin >> number;
    int answer;
    try {
        answer = fractalOfWhatNumber(number);
    } catch (invalid_argument e) {
        bool succes = false;
        cout << "Число должно быть факториалом. ";
        while (!succes) {
            try {
                cout << "Введите число: ";
                cin >> number;
                answer = fractalOfWhatNumber(number);
                succes = true;
            } catch (invalid_argument e) {
                cout << "Число должно быть факториалом. ";
            }
        }
    }
    cout << answer << endl;
    return 0;
}
int fractalOfWhatNumber(int number) {
    for (int pos = 0; true; pos++) {
        int factor = 0;
        try {
            factor = factorial(pos);
            cout << factor << endl;
        } catch (invalid_argument e) {
            throw e;
        }
        if (factor == number) {
            return pos;
        }
        if (factor > number) {
            throw invalid_argument("Number must be a factorial");
        }
    }
}

int factorial(int n) {
    if (n == 1 || n == 0) {
        return 1;
    } else if (n < 0) {
        throw invalid_argument("Number for fractal must be above -1");
    }
    return n * factorial(n - 1);
}
