#include <iostream>
#include <cstdio>
#include <iomanip> 
using namespace std;

int main() {

    int a;
    long b;
    char c;
    float d;
    double e;

    cin >> a >> b >> c >> d >> e;
    cout << a << "\n" << b << "\n" << c << endl;
    cout << fixed << setprecision(3) << d << endl;
    cout.unsetf(ios::floatfield);
    cout.precision(9);
    cout << e << endl;
    return 0;
}