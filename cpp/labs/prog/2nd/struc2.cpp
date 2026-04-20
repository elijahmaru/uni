#include <iostream>
using namespace std;

struct st {
    char value;
    st *next = nullptr;

    void init() {
        char inputValue;
        cout << "Введите строку: ";
        cin >> inputValue;
        st *pointer = this;
        while (inputValue != '.') {
            pointer->value = inputValue;
            pointer->next = new st;
            pointer = pointer->next;
            cin >> inputValue;
        }
        pointer->value = '.';
        pointer->next = nullptr;
    }

    void print() {
        st *point = this;
        while (point != nullptr) {
            cout << point->value;
            point = point->next;
        }
        cout << endl;
    }

    void myErase() {
        st *lastStartOfTheWord = this;
        st *pointer = this;
        while (pointer != nullptr && pointer->next != nullptr &&
               pointer->next->next != nullptr && pointer->next->value != '.') {
            if (pointer->value == pointer->next->next->value) {
                st *toDelete = pointer->next;
                pointer->next = toDelete->next;
                delete toDelete;
            } else {
                pointer = pointer->next;
            }
        }
    }
};

int main(int argc, char *argv[]) {
    st check;
    check.init();
    check.print();
    check.myErase();
    check.print();
    return 0;
}
