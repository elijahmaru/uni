#include <iostream>

using namespace std;

void outputRes(int *arr[3]);
int lcm(int fst, int snd);
int gcd(int fst, int snd);
int *foo(int fst, int snd);

int main(int argc, char *argv[]) {
    int a, b, c, d;
    cout << "Введите a: ";
    cin >> a;
    cout << "Введите b: ";
    cin >> b;
    cout << "Введите c: ";
    cin >> c;
    cout << "Введите d: ";
    cin >> d;
    cout << a << "/" << b << " + " << c << "/" << d << "=";
    return 0;
}

int lcm(int fst, int snd) { return (fst * snd) / gcd(fst, snd); }

int gcd(int fst, int snd) {
    if (fst == 0)
        return snd;
    return gcd(snd % fst, fst);
}

int *foo(int fstNum, int fstDiv) {
    int res[3] = {0, 0, 0};
    int least = lcm(fstDiv, sndDiv);
    int sum =
}
