#include <cstddef>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream file("task3_1.txt");
    if (!file) {
        throw invalid_argument("File must exist");
    }
    string inputString;
    getline(file, inputString);
    int maxLen = 0;
    int currentLen = 0;
    for (char currentChar : inputString) {
        if (currentChar == 'Z') {
            if (currentLen > maxLen) {
                maxLen = currentLen;
            }
            currentLen = 0;
        } else {
            currentLen++;
        }
    }
    if (maxLen < currentLen) {
        maxLen = currentLen;
    }
    cout << "Длина макс последовательности: " << maxLen << endl;
    return 0;
}
