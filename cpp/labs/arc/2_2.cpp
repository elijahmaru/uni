#include <cmath>
#include <cstdlib>
#include <iostream>
using namespace std;
int main() {
    cout << "Введите  B ";
    unsigned int B;
    cin >> B;
    int S = B >> 31;
    int E = (B >> 23) & ((1 << 8) - 1);
    int M = B & ((1 << 23) - 1);
    cout << S << " " << E << " " << M << endl;
    float F = pow(-1, S) * pow(2, E - 127) * (1 + float(M) / pow(2, 23));
    if ((E == 0) && (M != 0)) {
        F = pow(-1, S) * pow(2, -126) * (float(M) / pow(2, 23));
    }
    cout << F << endl;
    return 0;
}
