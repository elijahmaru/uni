#include <algorithm>
#include <cstddef>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const string one = "монета 1 рубль";
const string two = "монета 2 рубля";
const string five = "монета 5 рублей";
const string ten = "купюра 10 рублей";
const string fifty = "купюра 50 рублей";
const string hundred = "купюра 100 рублей";
const string twoHundred = "купюра 200 рублей";
const string fiveHundred = "купюра 500 рублей";
const string thousand = "купюра 1000 рублей";
const string twoThousand = "купюра 2000 рублей";
const string fiveThousand = "купюра 5000 рублей";
vector<string> banknotes = {fiveThousand, twoThousand, thousand, fiveHundred,
                            twoHundred,   hundred,     fifty,    ten,
                            five,         two,         one};

vector<string> leastBanknotesNeeded(int);
void printAnswer(const vector<string> &);

int main(int argc, char *argv[]) {
    int amount;
    cout << "Введите сумму: ";
    cin >> amount;
    vector<string> answer = leastBanknotesNeeded(amount);

    return 0;
}

vector<string> leastBanknotesNeeded(int summ) {
    vector<string> banknotesUsed;
    for (size_t i = 0; i < banknotes.size(); i++) {
        string banknote = banknotes.at(i);
        int value = stoi(
            banknote.substr(banknote.find(" ") + 1)
                .substr(0, banknote.substr(banknote.find(" ") + 1).find(" ")));
        while (summ % value > 0 && summ / value != 0) {
            summ %= value;
            banknotesUsed.push_back(banknote);
        }
    }
    return banknotesUsed;
}

void printAnswer(const vector<string> &answer) {
    int howMuch = 0;
    for (vector<string>::iterator it = banknotes.begin(); it != banknotes.end();
         ++it) {
        howMuch = count(answer.begin(), answer.end(), *it);
        if (howMuch) {
        
        }
    }
}
