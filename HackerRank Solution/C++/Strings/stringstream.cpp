#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    stringstream ss(str);
    vector<int> result; 
    char c;
    int temp;
    while (ss >> temp) {
        ss>>c;
        result.push_back(temp);
    }
    return result;
}

int main() {
    string str;
    cin >> str;
    
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}