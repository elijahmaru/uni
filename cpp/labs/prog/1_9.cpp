#include <iostream>
using namespace std;
int main(int argc, char *argv[]) {
    int age;
    cout << "введите цифру: ";
    cin >> age;
    if ((age < 20) && (age > 4)) {
        cout << "Вам " << age << " лет\n";
    } else {
        switch (age % 10) {
        case 1:
            cout << "Вам " << age << " год\n";
            break;
        case 2:
        case 3:
        case 4:
            cout << "Вам " << age << " годa\n";
            break;
        default:
            cout << "Вам " << age << " лет\n";
            break;
        }
    }
    return 0;
}
