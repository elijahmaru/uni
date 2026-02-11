// Вариант 5

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>

using namespace std;

int getRandomInt() { return -30 + rand() % (131); }
void outputVector(const vector<int> &);
void fillVector(vector<int> &);
void removeMin(vector<int> &);
vector<int>::iterator minElement(vector<int> &);
void insertMsinceX(vector<int> &, int, int);
void changeNear(vector<int> &, int);
vector<int> findValue(vector<int> &, int);

int main(int argc, char *argv[]) {
    srand(time(nullptr));
    vector<int> A(10);
    fillVector(A);
    outputVector(A);
    removeMin(A);
    outputVector(A);
    int m, x;
    cout << "Введите m: ";
    cin >> m;
    cout << "Введите x: ";
    cin >> x;
    insertMsinceX(A, m, x);
    outputVector(A);
    int pos;
    cout << "Введите позицию первого из пары для замены: ";
    cin >> pos;
    changeNear(A, pos);
    int val;
    cout << "Введите значение которое хотите найти: ";
    cin >> val;
    outputVector(findValue(A, val));
    return 0;
}

void outputVector(const vector<int> &vec) {
    cout << "{ ";
    for (vector<int>::const_iterator iterator = vec.begin();
         iterator != vec.end(); ++iterator) {
        cout << *iterator << ((iterator != vec.end() - 1) ? ", " : "}");
    }
}

void fillVector(vector<int> &vec) {
    for (vector<int>::iterator iterator = vec.begin(); iterator != vec.end();
         ++iterator) {
        *iterator = getRandomInt();
    }
}

vector<int>::iterator minElement(vector<int> &vec) {
    vector<int>::iterator iteratorToMin = vec.end();
    for (vector<int>::iterator iterator = vec.begin(); iterator != vec.end();
         iterator++) {
        if (*iteratorToMin > *iterator) {
            iteratorToMin = iterator;
        }
    }
    return iteratorToMin;
}

void removeMin(vector<int> &vec) {
    if (minElement(vec) == vec.end())
        return;
    vec.erase(minElement(vec));
}

void insertMsinceX(vector<int> &vec, int m, int x) {
    if (m == 0) {
        return;
    }
    vector<int> values(m);
    for (vector<int>::iterator iterator = values.begin();
         iterator != values.end(); ++iterator) {
        cout << "Введите значение: ";
        cin >> *iterator;
    }
    vec.insert(vec.begin() + x, values.begin(), values.end());
}

void changeNear(vector<int> &vec, int pos) {
    if ((pos < 0) || (pos >= vec.size() - 1)) {
        return;
    }
    int buff = vec[pos];
    vec[pos] = vec[pos + 1];
    vec[pos + 1] = buff;
}

vector<int> findValue(vector<int> &vec, int val) {
    vector<int> vectorOfIterators;
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i] == val) {
            vectorOfIterators.push_back(i);
        }
    }
    return vectorOfIterators;
}
