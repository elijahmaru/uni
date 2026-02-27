#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int x = 10;
    int *p = &x;
    *p += *(&x);
    cout << x;
}
