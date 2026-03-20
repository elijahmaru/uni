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

int main(int argc, char *argv[]) {
    leastBanknotesNeeded(10);
    return 0;
}

vector<string> leastBanknotesNeeded(int summ) {
    vector<string> banknotesUsed;
    for (size_t i = 0; i < banknotes.size(); i++) {
        string banknote = banknotes.at(i);
        int value = stoi(
            banknote.substr(banknote.find(" ") + 1)
                .substr(0, banknote.substr(banknote.find(" ") + 1).find(" ")));
        cout << value << endl;
        while (condition) {
        
        }
    }
    return banknotesUsed;
}
