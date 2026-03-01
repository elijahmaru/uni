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
vector<int>::iterator maxElement(vector<int> &);
void insertMatX(vector<int> &, int, int);
void changeNear(vector<int> &, int);
vector<int> findValue(vector<int> &, int);
// Варина 3
void removeStartingFrom(vector<int> &, int, int);
void insertAtStart(vector<int> &, int);
void changeMaxAndMin(vector<int> &);
int firstEvenAt(vector<int> &);

int main(int argc, char *argv[]) {
    srand(time(nullptr));
    vector<int> A(10);
    fillVector(A);
    outputVector(A);
    vector<int> buff = A;
    removeMin(A);
    outputVector(A);
    A = buff;
    int m, x;
    cout << "Введите m: ";
    cin >> m;
    cout << "Введите x: ";
    cin >> x;
    insertMatX(A, m, x);
    outputVector(A);
    A = buff;
    int pos;
    cout << "Введите позицию первого из пары для замены: ";
    cin >> pos;
    changeNear(A, pos);
    outputVector(A);
    A = buff;
    int val;
    cout << "Введите значение которое хотите найти: ";
    cin >> val;
    outputVector(findValue(A, val));
    A = buff;
    cout << "Варинат №3\n";
    fillVector(A);
    int M, K;
    do {
        cout << "Введите сколько элементов хотите удалить :";
        cin >> M;
        cout << "Введите с какого индекса хотите удалить :";
    } while (M + K > A.size());
    removeStartingFrom(A, M, K);
    outputVector(A);
    int X;
    cout << "Сколько элементов хотите добавить :";
    cin >> X;
    insertAtStart(A, X);
    outputVector(A);
    changeMaxAndMin(A);
    outputVector(A);
    cout << "Первый чётный элемент: " << A.at(firstEvenAt(A)) << endl;
    return 0;
}

void outputVector(const vector<int> &vec) {
    cout << "{ ";
    for (vector<int>::const_iterator iterator = vec.begin();
         iterator != vec.end(); ++iterator) {
        cout << *iterator << ((iterator != vec.end() - 1) ? ", " : "}\n");
    }
}

void fillVector(vector<int> &vec) {
    for (vector<int>::iterator iterator = vec.begin(); iterator != vec.end();
         ++iterator) {
        *iterator = getRandomInt();
    }
}

vector<int>::iterator minElement(vector<int> &vec) {
    vector<int>::iterator iteratorToMin = vec.begin();
    for (vector<int>::iterator iterator = vec.begin(); iterator != vec.end();
         ++iterator) {
        if (*iteratorToMin > *iterator) {
            iteratorToMin = iterator;
        }
    }
    return iteratorToMin;
}

vector<int>::iterator maxElement(vector<int> &vec) {
    vector<int>::iterator iteratorToMax = vec.begin();
    for (vector<int>::iterator iterator = vec.begin(); iterator != vec.end();
         ++iterator) {
        if (*iteratorToMax < *iterator) {
            iteratorToMax = iterator;
        }
    }
    return iteratorToMax;
}
void removeMin(vector<int> &vec) {
    int minValue = *minElement(vec);
    for (vector<int>::iterator iterator = vec.begin(); iterator != vec.end();) {
        if (*iterator == minValue) {
            iterator = vec.erase(iterator);
        } else {
            ++iterator;
        }
    }
}

void insertMatX(vector<int> &vec, int m, int x) {
    if (m == 0) {
        return;
    }
    if (x < 0 || x > vec.size() - 1)
        return;
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
    vector<int> vectorOfIndexes;
    for (int i = 0; i < vec.size(); i++) {
        if (vec[i] == val) {
            vectorOfIndexes.push_back(i);
        }
    }
    return vectorOfIndexes;
}
// Вариант 3
void removeStartingFrom(vector<int> &vec, int M, int K) {
    for (int i = 0; i < M && i + K < vec.size(); i++) {
        vec.erase(vec.begin() + K);
    }
}

void insertAtStart(vector<int> &vec, int X) {
    vector<int> values(X);
    for (vector<int>::iterator iterator = values.begin();
         iterator != values.end(); ++iterator) {
        cout << "Введите значение: ";
        cin >> *iterator;
    }
    vec.insert(vec.begin(), values.begin(), values.end());
}

void changeMaxAndMin(vector<int> &vec) {
    vector<int>::iterator itToMin = minElement(vec);
    vector<int>::iterator itToMax = maxElement(vec);
    int buff = *itToMax;
    *itToMax = *itToMin;
    *itToMin = buff;
}

int firstEvenAt(vector<int> &vec) {
    for (size_t i = 0; i < vec.size(); i++) {
        if (vec.at(i) % 2 == 0) {
            return i;
        }
    }
    return -1;
}
