#include <cmath>
#include <cstdlib>
#include <iostream>
using namespace std;
int main() {
    double x, y, r;
    cout << "x = ";
    cin >> x;
    cout << "y = ";
    cin >> y;
    cout << "r = ";
    cin >> r;
    if (((pow(x + r, 2) + pow(y + r, 2) <= pow(r, 2)) ||
         (pow(x - r, 2) + pow(y - r, 2) <= pow(r, 2))) &&
        !((abs(x) < 1) && (abs(y) < 1))) {
        cout << "3. yes" << endl;
    } else {
        cout << "3. no" << endl;
    }
    if ((pow(x, 2) + pow(y, 2) >= pow(r, 2)) &&
        (pow(x, 2) + pow(y, 2) <= pow(2 * r, 2)) && ((x * y) >= 0)) {
        cout << "12. yes";
    } else {
        cout << "12. no";
    }
    if ((y >= (pow(x - r, 2) - r)) && (abs(y) <= x)) {
        cout << "9. yes";
    } else {
        cout << "9. no";
    }
}
