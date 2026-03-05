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

vector<string> leastBanknotesNeeded(int);

int main(int argc, char *argv[]) { return 0; }
// сделать for loop для банкнот и из значений
vector<string> leastBanknotesNeeded(int summ) {
    vector<string> banknotes;
    for (size_t i = 0; i < length; i++) {
        
    }
    while (summ % 5000 != 0 && summ > 5000) {
        banknotes.push_back(fiveThousand);
    }
    return banknotes;
}
