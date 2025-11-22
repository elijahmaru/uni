#include <cmath>
#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
    float a;
    cout << "Введите a = ";
    cin >> a;
    unsigned int S = (a >= 0) ? 0 : 1;
    int k = log2(a) / 1;
    cout << k << endl;
    unsigned int E;
    unsigned int M;
    if (k >= -126) {
        E = k + 127;
        M = (abs(a) / (pow(2, k)) - 1) * pow(2, 23);
    } else {
        E = 0;
        M = (abs(a) / pow(2, -126)) * pow(2, 23);
    }
    cout << S << " " << E << " " << M << endl;
    return 0;
}
