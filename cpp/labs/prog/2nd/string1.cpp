#include <iostream>
#include <string>
// 11
using namespace std;

int findWord(string);

int main(int argc, char *argv[]) {
    string text;
    cout << "Введите текст: ";
    getline(cin, text);
    int count = findWord(text);
    if (count != 0) {
        cout << "Количество слов :" << findWord(text);
    } else {
        cout << "Таких слов нет";
    }
    return 0;
}

int findWord(string text) {
    int count = 0;
    for (size_t i = 0; i < text.length(); i++) {
        int startOfTheWord = text.find("м", i);
        int endOfTheWord = text.find(" ") - 1;
        while (text.at(endOfTheWord) == ',' || text.at(endOfTheWord) == '.' ||
               text.at(endOfTheWord) == '?' || text.at(endOfTheWord) == '!') {
            --endOfTheWord;
        }
        if (text.substr(endOfTheWord, 1) == "а") {
            count++;
        }
        i = endOfTheWord;
    }
    return count;
}
