#include <cstddef>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct route {
    int number;
    string type;
    string destanation;
    int timeOfDeparture;
    int timeOfArrival;
};

vector<route> routes = {
    {1, "City Bus", "Moscow", 800, 1700},
    {2, "Mini Bus", "Kazan", 810, 1310},
    {3, "Express", "Novgorod", 220, 920},
    {4, "City Bus", "Sochi", 230, 2130},
    {5, "Mini Bus", "Saint-Petersburg", 440, 2340},
    {6, "Express", "Moscow", 850, 1450},
    {7, "City Bus", "Kazan", 660, 2330},
};

vector<int> getBuses(string, int);

int main(){
    int time;
    do {
        cout << "Введите время: ";
        cin >> time;
    }while (time > 2400);
    string dest;
    getline(cin, dest);
}

vector<int> getBuses(string dest, int time){
    vector<int> buses;
    for (size_t pos = 0; pos < routes.size(); pos++) {
        string busDest = routes[pos].destanation;
        int timeOfArrival = routes[pos].timeOfArrival;
        int busNumber = routes[pos].number;
        if (timeOfArrival <= time && busDest == dest) {
            buses.push_back(busNumber);
        }
    }
    return buses;
}
