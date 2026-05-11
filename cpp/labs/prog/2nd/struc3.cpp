#include <csignal>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

class train {
    int number;
    string destination;
    int dayOfDeparture;
    int timeOfDeparture;
    int dayOfArrival;
    int timeOfArrival;
    int amountOfSeats;
    int amountOfFreeSeats;

  public:
    train(int number, string destination, int dayOfDeparture,
          int timeOfDeparture, int dayOfArrival, int timeOfArrival,
          int amountOfSeats, int amountOfFreeSeats) {
        if (dayOfDeparture > 365) {
            throw invalid_argument(
                "Day of departure exceeds amount of days in a year");
        }
        if (dayOfArrival > 365 || dayOfArrival < dayOfDeparture) {
            throw invalid_argument(
                "Day of arrival exceeds amount of days in a year");
        }
        if (timeOfDeparture > 2400 || timeOfArrival > 2400 ||
            (timeOfArrival < timeOfDeparture &&
             dayOfArrival == dayOfDeparture)) {
            throw invalid_argument("Time is impossible");
        }
        if (amountOfSeats < amountOfFreeSeats) {
            throw invalid_argument("Impossible amount of free seats");
        }
        this->number = number;
        this->destination = destination;
        this->dayOfDeparture = dayOfDeparture;
        this->timeOfDeparture = timeOfDeparture;
        this->dayOfArrival = dayOfArrival;
        this->timeOfArrival = timeOfArrival;
        this->amountOfSeats = amountOfSeats;
        this->amountOfFreeSeats = amountOfFreeSeats;
    }
    int getTimeOfDeparture() { return this->timeOfDeparture; }
    int getTimeOfArrival() { return this->timeOfArrival; }
    string getDestination() { return this->destination; }
    int getDayOfArrival() { return this->dayOfArrival; }
    int getDayOfDeparture() { return this->dayOfDeparture; }
    string getFormatedTimeOfArrival() const {
        string result;
        if (this->timeOfArrival / 100 < 10) {
            result = "0";
        }
        result += to_string(this->timeOfArrival / 100) + ":";
        if (this->timeOfArrival % 100 < 10) {
            result += "0";
        }
        result += to_string(this->timeOfArrival % 100);
        return result;
    }
    string getFormatedTimeOfDeparture() const {
        string result;
        if (this->timeOfDeparture / 100 < 10) {
            result = "0";
        }
        result += to_string(this->timeOfDeparture / 100) + ":";
        if (this->timeOfArrival % 100 < 10) {
            result += "0";
        }
        result += to_string(this->timeOfDeparture % 100);
        return result;
    }
    bool hasFreeSeats() {
        if (this->amountOfFreeSeats != 0) {
            return true;
        }
        return false;
    }
    void show() const {
        cout << left << setw(8) << this->number << setw(18) << this->destination
             << setw(8) << this->dayOfDeparture << setw(10)
             << this->getFormatedTimeOfDeparture() << setw(8)
             << this->dayOfArrival << setw(10)
             << this->getFormatedTimeOfArrival() << setw(10)
             << this->amountOfSeats << setw(10) << this->amountOfFreeSeats
             << endl;
    }
};
vector<train> trainsTo(const vector<train> arrOfTrains, string destination) {
    vector<train> result;
    for (train current : arrOfTrains) {
        if (current.getDestination() == destination) {
            result.push_back(current);
        }
    }
    return result;
}

vector<train> trainsToAfter(const vector<train> arrOfTrains, string destination,
                            int time, int date) {
    vector<train> newArrOfTrains = trainsTo(arrOfTrains, destination);
    vector<train> result;
    for (train current : arrOfTrains) {
        if (current.getTimeOfDeparture() > time &&
            current.getDayOfDeparture() == date) {
            result.push_back(current);
        }
    }
    return result;
}

vector<train> trainsToWihtEmptySeats(const vector<train> arrOfTrains,
                                     string destination) {
    vector<train> newArrOfTrains = trainsTo(arrOfTrains, destination);
    vector<train> result;
    for (train current : arrOfTrains) {
        if (current.hasFreeSeats()&& destination == current.getDestination()) {
            result.push_back(current);
        }
    }
    return result;
}

void showTable(const vector<train> &trains) {
    cout << left << setw(8) << "No" << setw(18) << "Destination" << setw(8)
         << "DepDay" << setw(10) << "DepTime" << setw(8) << "ArrDay" << setw(10)
         << "ArrTime" << setw(10) << "Seats" << setw(10) << "Free" << endl;
    for (const train &t : trains) {
        t.show();
    }
}
int main(int argc, char *argv[]) {
    vector<train> trains = {train(101, "MOW", 12, 830, 12, 1230, 200, 45),
                            train(102, "MOW", 12, 1400, 12, 1800, 200, 0),
                            train(103, "MOW", 13, 900, 13, 1300, 180, 20),
                            train(104, "MOW", 14, 2200, 15, 600, 150, 0),
                            train(201, "SBP", 15, 700, 15, 1100, 220, 80),
                            train(202, "SBP", 15, 1500, 15, 1900, 220, 0),
                            train(203, "SBP", 16, 600, 16, 1000, 220, 12),
                            train(204, "LBP", 16, 2100, 17, 130, 220, 0),
                            train(301, "KZN", 20, 500, 20, 1100, 300, 150),
                            train(302, "KZN", 20, 1200, 20, 1800, 300, 0),
                            train(303, "KZN", 21, 745, 21, 1345, 280, 33),
                            train(401, "ASTR", 25, 1000, 25, 1400, 160, 60),
                            train(402, "ASTR", 25, 1800, 25, 2200, 160, 0),
                            train(403, "ASTR", 26, 815, 26, 1215, 160, 10),
                            train(501, "NVGR", 30, 600, 30, 1400, 250, 25),
                            train(502, "NVGR", 30, 1600, 30, 2350, 250, 0),
                            train(503, "NVGR", 31, 900, 31, 1700, 250, 70)};
    string destination;
    cout << "Изначальное расписание\n";
    showTable(trains);
    cout << "Введите назначение: ";
    getline(cin, destination);
    cout << "Расписания до пункта\n";
    showTable(trainsTo(trains, destination));
    string userTime;
    cout << ("Введите время: ");
    getline(cin, userTime);
    string userDate;
    cout << ("Введите день:  ");
    getline(cin, userDate);
    int date = stoi(userDate);
    int time = stoi(userTime.substr(3, 2)) + stoi(userTime.substr(0, 2)) * 100;
    showTable(trainsToAfter(trains, destination, time, date));
    cout << "Поезда со свободными местами:\n";
    showTable(trainsToWihtEmptySeats(trains, destination));
    return 0;
}
