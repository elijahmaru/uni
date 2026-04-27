#include <iostream>
using namespace std;

struct charChain {
    char value;
    charChain *next = nullptr;

    void init() {
        char inputValue;
        cout << "Введите строку и закончите её точкой: ";
        cin >> inputValue;
        charChain *pointer = this;
        while (inputValue != '.') {
            pointer->value = inputValue;
            pointer->next = new charChain;
            pointer = pointer->next;
            cin >> inputValue;
        }
        pointer->value = '.';
        pointer->next = nullptr;
    }

    void print() {
        cout << "prep to output\n";
        charChain *point = this;
        while (point != nullptr) {
            cout << point->value;
            point = point->next;
        }
        cout << endl;
    }

    void myErase() {
        cout << "erase started\n";
        charChain *lastStartOfTheWord = this;
        charChain *pointer = this;
        while (pointer != nullptr && pointer->next != nullptr &&
               pointer->next->next != nullptr && pointer->next->value != '.') {
            cout << "erase in progress\n";
            if (pointer->value == pointer->next->next->value) {
                charChain *toDelete = pointer->next;
                pointer->next = toDelete->next;
                delete toDelete;
            } else {
                pointer = pointer->next;
            }
        }
    }
/*
    ~charChain() {
        charChain *pointer = this->next;
        while (pointer != nullptr) {
            charChain *toDelete = pointer;
            pointer = pointer->next;
            delete toDelete;
        }
    }
*/
};

int main(int argc, char *argv[]) {
    charChain check;
    check.init();
    check.print();
    check.myErase();
    check.print();
    return 0;
}
