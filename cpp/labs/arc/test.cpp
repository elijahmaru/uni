#include <iostream>
#include <ostream>
using namespace std;
int inc(const int *arr) {
    cout << arr[0] << endl;
    return arr[0];
}
int main(int argc, char *argv[]) {
    int *i = new int[4];
    inc(i);
}
