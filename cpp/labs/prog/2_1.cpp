#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

void outputArray(int array[]) {
    cout << "[";
    for (int i = 0; i < 7; i++) {
        cout << array[i] << ((i == 6) ? "" : ", ");
    }
    cout << "]" << endl;
}

bool checkSort(int arr[]) {
    for (int i = 1; i < 7; i++) {
        if (arr[i - 1] > arr[i]) {
            return false;
        }
    }
    return true;
}

int main(int argc, char *argv[]) {
    int numbers[7];
    for (int i = 0; i < 7; i++) {
        cout << "numbers[" << i << "] = ";
        cin >> numbers[i];
    }
    outputArray(numbers);

    cout << "Метод простого выбора:" << endl;
    int simpleSort[7];
    for (int i = 0; i < 7; i++) {
        simpleSort[i] = numbers[i];
    }
    outputArray(simpleSort);
    int sorted{0};
    int posMin{0};
    int buffer{0};
    while (!checkSort(simpleSort)) {
        posMin = sorted;
        for (int i = sorted + 1; i < 7; i++) {
            if (simpleSort[i] < simpleSort[posMin])
                posMin = i;
        }
        if (sorted != posMin) {
            buffer = simpleSort[posMin];
            simpleSort[posMin] = simpleSort[sorted];
            simpleSort[sorted] = buffer;
        }
        cout << (++sorted) << ". ";
        outputArray(simpleSort);
    }
    cout << "Результат: ";
    outputArray(simpleSort);

    cout << "\nМетод простого включения (сдвиг-вставка):" << endl;
    int shiftInsert[7];
    for (int i = 0; i < 7; i++) {
        shiftInsert[i] = numbers[i];
    }
    outputArray(shiftInsert);
    sorted = 0;
    buffer = 0;
    int posForUnsort{};
    while (!checkSort(shiftInsert)) {
        posForUnsort = sorted + 1;
        for (int i = 0; i <= sorted; i++) {
            if (shiftInsert[i] >= shiftInsert[sorted + 1]) {
                posForUnsort = i;
                break;
            }
        }
        buffer = shiftInsert[sorted + 1];
        for (int i = sorted; i >= posForUnsort; i--) {
            shiftInsert[i + 1] = shiftInsert[i];
        }
        shiftInsert[posForUnsort] = buffer;
        cout << (++sorted) << ". ";
        outputArray(shiftInsert);
    }
    cout << "Результат: ";
    outputArray(shiftInsert);

    cout << "\nМетод простого обмена:" << endl;
    int bubbleSort[7];
    for (int i = 0; i < 7; i++) {
        bubbleSort[i] = numbers[i];
    }
    outputArray(bubbleSort);
    sorted = 0;
    buffer = 0;
    while (true) {
        bool count{0};
        for (int i = 6; i > 0; i--) {
            if (bubbleSort[i] < bubbleSort[i - 1]) {
                buffer = bubbleSort[i - 1];
                bubbleSort[i - 1] = bubbleSort[i];
                bubbleSort[i] = buffer;
                count = true;
            }
        }
        cout << (++sorted) << ". ";
        outputArray(bubbleSort);
        if (!count)
            break;
    }
    cout << "Результат: ";
    outputArray(bubbleSort);
    return 0;
}
