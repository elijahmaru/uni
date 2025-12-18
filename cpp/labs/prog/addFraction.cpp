#include <iostream>

using namespace std;

void outputRes(int arr[3]);
int lcm(int fst, int snd);
int gcd(int fst, int snd);
int *foo(int fstDiv, int fstNum, int sndDiv, int sndNum);

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
    cout << a << "/" << b << " + " << c << "/" << d << " = ";
    outputRes(foo(a, b, c, d));
    return 0;
}

int lcm(int fst, int snd) { return (fst * snd) / gcd(fst, snd); }

int gcd(int fst, int snd) {
    if (fst == 0)
        return snd;
    return gcd(snd % fst, fst);
}

int *foo(int fstNum, int fstDiv, int sndNum, int sndDiv) {
    static int res[3] = {0, 0, 0};
    int least = lcm(fstDiv, sndDiv);
    res[2] = least;
    int sum = fstNum * (least / fstDiv) + sndNum * (least / sndDiv);
    res[0] = sum / least;
    res[1] = sum % least;
    return res;
}

void outputRes(int arr[3]) {
    if (arr[0] != 0) {
        cout << arr[0] << " ";
    }
    int num = arr[1];
    int div = arr[2];
    if (arr[1] != 0) {
        if (arr[2] % arr[1] == 0) {
            num /= gcd(arr[1], arr[2]);
            div /= gcd(arr[1], arr[2]);
        }
        cout << num << "/" << div;
    }
    cout << "\n";
    return;
}
