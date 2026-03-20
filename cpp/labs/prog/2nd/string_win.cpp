#include <cctype>
#include <cstddef>
#include <iostream>
#include <string>
#include <vector>
#include <windows.h>

// 11
using namespace std;

int findWord(string);
string findMostStartingChar(string);
int indexOfMax(const vector<int> &);

int main(int argc, char *argv[]) {
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    cout << "Задание №1\n";
    string text;
    cout << "Введите текст: ";
    getline(cin, text);
    int count = findWord(text);
    if (count != 0) {
        cout << "Количество слов :" << count << endl;
    } else {
        cout << "Таких слов нет\n";
    }
    cout << "Задание №2\n";
    cout << "Введите текст: ";
    getline(cin, text);
    cout << "Больше всего слов начинается на " << findMostStartingChar(text)
         << endl;
    return 0;
}

int findWord(string text) {
    int count = 0;
    size_t i = 0;
    while (i < text.length()) {
        int startOfTheWord = text.find("м", i);
        if (startOfTheWord == string::npos) {
            return count;
        }
        int endOfTheWord = text.find("а", startOfTheWord);
        if (endOfTheWord == string::npos) {
            return count;
        }
        while (endOfTheWord > startOfTheWord &&
               (text.at(endOfTheWord) == '.' || text.at(endOfTheWord) == ',' ||
                text.at(endOfTheWord) == '?' || text.at(endOfTheWord) == '!')) {
            endOfTheWord--;
        }
        if (text.substr(startOfTheWord, endOfTheWord - startOfTheWord + 1)
                .find(" ") == string::npos)
            count++;
        i = startOfTheWord + 1;
    }
    return count;
}

int indexOfMax(const vector<int> &vec) {
    int index = 0;
    for (size_t i = 0; i < vec.size(); i++) {
        if (vec.at(index) < vec.at(i)) {
            index = i;
        }
    }
    return index;
}

string findMostStartingChar(string text) {
    if (text.at(text.length() - 1) == ' ') {
        text = text.substr(0, text.length() - 1);
    }
    vector<int> times;
    string startChars;
    times.push_back(1);
    startChars += text.at(0);
    for (size_t i = 1; i < text.length() && text.find(" ", i) != string::npos;
         i++) {
        size_t pos = text.find(" ", i);
        if (pos == string::npos || pos + 1 >= text.length())
            break;

        char potStart = text.at(pos + 1);
        if (startChars.find(potStart) != string::npos) {
            times.at(startChars.find(potStart))++;
        } else {
            times.push_back(1);
            startChars += potStart;
        }
    }
    return startChars.substr(indexOfMax(times), 1);
}
