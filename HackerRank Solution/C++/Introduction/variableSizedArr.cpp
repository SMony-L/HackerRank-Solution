#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iterator>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n,q,k;
    int val;
    int which, index;
    cin >> n >> q;

    vector<vector<int> > arr;
    for (int i = 0; i < n; i++){
        cin >> k;
        vector<int> newVec;
        for (int j = 0; j < k; j++) {
            cin >> val;
            newVec.push_back(val);
        }
        arr.push_back(newVec);
    }
    for (int k = 0; k < q; k++) {
        cin >> which >> index;
        cout << arr[which][index] << endl;
    }
    
    return 0;
}
