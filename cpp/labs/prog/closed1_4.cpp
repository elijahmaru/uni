#include <cmath>
#include <iostream>
using namespace std;
int main() {
    cout << (pow(2, 2) / 3) << endl;
    int x;
    cout << "1. " << endl << "x = ";
    cin >> x;
    int a1{};
    for (int i = 0; i <= 10; i++)
        a1 += (11 - i) * pow(x, i);
    cout << a1 << endl;

    cout << "3. " << endl << "x = ";
    cin >> x;
    float a3 = pow(x, 2);
    for (int j = 8; j >= 1; j--)
        a3 = pow(x, 2) + pow(2, j) / 2;
    a3 = x / a3;
    cout << a3 << endl;

    float a;
    cout << "5. " << endl << "a = ";
    cin >> a;
    int n;
    cout << "n = ";
    cin >> n;
    float a5{}, p{1};
    for (int i = 0; i <= n; i++) {
        p *= (a + i);
        a5 += 1 / p;
    }
    cout << a5 << endl;

    float a7{};
    cout << "7. ";
    for (int c = 99; c != 0; c -= 3)
        a7 = sqrt(c + a7);
    cout << a7 << endl;

    float a9{};
    for (int i = 0; i < 10000; i++) {
        if (i % 2 == 1)
            a9 += 1. / i;
        else
            a9 -= 1. / i;
    }
    cout << a9 << endl;
}
