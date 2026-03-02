#include <cctype>
#include <iostream>
#include <string>
#include <vector>
// 11
using namespace std;

string findMostStartingChar(string);
int indexOfMax(const vector<int> &);

int main(int argc, char *argv[]) {
    string text;
    cout << "Введите текст: ";
    getline(cin, text);
    cout << "Больше всего слов начинается на " << findMostStartingChar(text);
    return 0;
}

int indexOfMax(const vector<int> &vec) {
    int index = 0;
    for (int i = 0; i < vec.size(); i++) {
        if (vec.at(index) < vec.at(i)) {
            index = i;
        }
    }
    return index;
}

string findMostStartingChar(string text) {
    vector<int> times;
    string chararcter;
    chararcter += text.at(0);
    times.at(0) = 1;
    for (int i = 0; i < text.length() && text.find(" ") + 1 == text.length();
         i++) {
        char startOfTheWord = tolower(text.at(text.find(" ") + 1));
        if (chararcter.find(startOfTheWord) != string::npos) {
            times.at(chararcter.find(startOfTheWord))++;
        } else {
            chararcter += startOfTheWord;
            times.push_back(1);
        }
    }
    return chararcter.substr(indexOfMax(times), 1);
}
