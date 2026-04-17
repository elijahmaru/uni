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
    int left = 0;
    int zCount = 0;
    int maxLen = 0;

    for (int right = 0; right < inputString.size(); right++) {
        if (inputString[right] == 'Z') {
            zCount++;
        }
        while (zCount > 2) {
            if (inputString[left] == 'Z') {
                zCount--;
            }
            left++;
        }

        maxLen = max(maxLen, right - left + 1);
        if (maxLen < right - left + 1) {
            maxLen = right - left + 1;
        }
    }

    cout << "Длина макс последовательности: " << maxLen << endl;
    return 0;
}
