#include <iostream>
using namespace std;
int main(int argc, char *argv[]) {
    int month{};
    do {
        cout << "Введите месяц рождения(номер): ";
        cin >> month;
    } while ((month < 1) | (month > 12));
    int date{};
    do {
        cout << "Введите дату рождения: ";
        cin >> date;
    } while ((date < 1) | (date > 31));

    int hash = (month - 1) * 31 + date;

    switch (hash) {
    case 21 ... 51:
        cout << "водолей" << endl;
        break;
    case 52 ... 82:
        cout << "рыбы" << endl;
        break;
    case 83 ... 113:
        cout << "овен" << endl;
        break;
    case 114 ... 144:
        cout << "телец" << endl;
        break;
    case 145 ... 176:
        cout << "близнецы" << endl;
        break;
    case 177 ... 208:
        cout << "рак" << endl;
        break;
    case 209 ... 240:
        cout << "лев" << endl;
        break;
    case 241 ... 271:
        cout << "дева" << endl;
        break;
    case 272 ... 302:
        cout << "весы" << endl;
        break;
    case 303 ... 332:
        cout << "скорпион" << endl;
        break;
    case 333 ... 362:
        cout << "стрелец" << endl;
        break;
    default:
        cout << "козерог" << endl;
    } return 0;
}
