#include <iostream>
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
    text = " " + text + " ";
    int amount = 0;
    size_t i = 0;
    for (vector<string>::iterator it = punctuation.begin();
         it != punctuation.end(); ++it) {
        while (text.find(*it) != string::npos) {
            int deleteChar = text.find(*it);
            text = text.substr(0, deleteChar) + text.substr(deleteChar + 1);
        }
    }
    cout << text << endl;
    while (i < 10) {
        int startOfTheWord = (text.find(" м", i) < text.find(" М", i))
                                 ? text.find(" м", i)
                                 : text.find(" М", i);
        if (startOfTheWord == string::npos)
            return amount;
        int endOfTheWord = text.find("а ", endOfTheWord);
        if (endOfTheWord == string::npos)
            return amount;
        cout << text.substr(startOfTheWord, endOfTheWord - startOfTheWord)
             << "end" << endl;
        i = endOfTheWord;
    }
    return amount;
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
