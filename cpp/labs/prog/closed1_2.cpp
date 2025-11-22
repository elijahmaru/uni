#include <cmath>
#include <iostream>
using namespace std;
int main() {
    double a;
    cout << "a = ";
    cin >> a;
    cout << "3. ";
    if (abs(a) >= 2)
        cout << (abs(a) - 2) << endl;
    else
        cout << sqrt(4 - pow(a, 2)) << endl;
    cout << "10. ";
    if (abs(a) >= 3)
        cout << (abs(a) - 3) << endl;
    else if (abs(a) >= 1)
        cout << (sqrt(1 - pow(abs(a) - 2, 2))) << " / "
             << (-sqrt(1 - pow(abs(a) - 2, 2))) << endl;
    else
        cout << ((1 - pow(a, 2) / 2)) << endl;
}
