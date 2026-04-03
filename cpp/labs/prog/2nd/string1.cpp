#include <cctype>
#include <cstddef>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

// 11
using namespace std;

vector<string> punctuation = {".", ",", "?", "!", ":", ";"};

int findWord(string);
string findMostStartingChar(string);
int indexOfMax(const vector<int> &);

int main(int argc, char *argv[]) {
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
    for (vector<string>::iterator it = punctuation.begin();
         it != punctuation.end(); ++it) {
        while (text.find(*it) != string::npos) {
            int deleteChar = text.find(*it);
            text = text.substr(0, deleteChar) + text.substr(deleteChar + 1);
        }
    }
    if (text.length() == 0) {
        return 0;
    }
    int amount = 0;
    string word;
    stringstream ssText(text);
    while (ssText >> word) {
        if (word.length() >= 2) {
            string fst = word.substr(0, 1);
            string last = word.substr(word.length() - 1, 1);
            if ((fst == "м" || fst == "М") && last == "а") {
                amount++;
                cout << word << endl;
            }
        }
    }
    return amount;
}

int indexOfMax(const vector<int> &vec) {
    int index = 0;
    for (size_t pos = 0; pos < vec.size(); pos++) {
        if (vec.at(index) < vec.at(pos)) {
            index = pos;
        }
    }
    return index;
}

string findMostStartingChar(string text) {
    for (vector<string>::iterator it = punctuation.begin();
         it != punctuation.end(); ++it) {
        while (text.find(*it) != string::npos) {
            int deleteChar = text.find(*it);
            text = text.substr(0, deleteChar) + text.substr(deleteChar + 1);
        }
    }
    if (text.length() == 0) {
        return "";
    }
    for (int pos = 0; pos < text.length() && text.at(pos) == ' ';) {
        text.erase(0, 1);
    }
    if (text.length() == 0) {
        return "";
    }
    for (int pos = text.length() - 1; pos >= 0 && text.at(pos) == ' '; pos--) {
        text.erase(pos, 1);
    }
    if (text.length() == 0) {
        return "";
    }
    for (size_t pos = 0; pos < text.length(); pos++) {
        text[pos] = tolower(text.at(pos));
    }
    vector<int> howMany;
    string startChar;
    string word;
    stringstream ssText(text);
    while (ssText >> word) {
        size_t pos = startChar.find(word.substr(0, 1));
        if (pos == string::npos) {
            startChar += word.substr(0, 1);
            howMany.push_back(1);
        } else {
            howMany[pos]++;
        }
    }
    return startChar.substr(indexOfMax(howMany), 1);
}
