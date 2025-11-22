#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main(){
    float x;
	cout<<"x=";
    cin>>x;
    double s = 1 + x + pow(x, 2)/2 + pow(x, 3)/(2*3) + pow(x, 4)/(2*3*4);
    cout<<"s="<<fixed<<setprecision(2)<<s<<endl;
    cout<<"y=";
    float y;
    cin>>y;
    double z = x * (sin(pow(x, 3)) + pow(cos(y), 2));
    cout<<"z="<<fixed<<setprecision(2)<<z;
}
