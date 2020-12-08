// #include <bits/stdc++.h>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    string allString[10] = {"Greater than 9", "one","two","three","four","five","six","seven","eight","nine"};
    if (n > 9) {
        cout << allString[0];
    } else {
        cout << allString[n] << endl;
    }
    

    return 0;
}
