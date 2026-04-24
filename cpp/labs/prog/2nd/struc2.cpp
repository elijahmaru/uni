#include <iostream>
using namespace std;

struct str {
    char value;
    str *next = nullptr;

    void init() {
        char inputValue;
        cout << "Введите строку: ";
        cin >> inputValue;
        str *pointer = this;
        while (inputValue != '.') {
            pointer->value = inputValue;
            pointer->next = new str;
            pointer = pointer->next;
            cin >> inputValue;
        }
        pointer->value = '.';
        pointer->next = nullptr;
    }

    void print() {
        str *point = this;
        while (point != nullptr) {
            cout << point->value;
            point = point->next;
        }
        cout << endl;
    }

    void myErase() {
        str *lastStartOfTheWord = this;
        str *pointer = this;
        while (pointer != nullptr && pointer->next != nullptr &&
               pointer->next->next != nullptr && pointer->next->value != '.') {
            if (pointer->value == pointer->next->next->value) {
                str *toDelete = pointer->next;
                pointer->next = toDelete->next;
                delete toDelete;
            } else {
                pointer = pointer->next;
            }
        }
    }
};

int main(int argc, char *argv[]) {
    str check;
    check.init();
    check.print();
    check.myErase();
    check.print();
    return 0;
}
