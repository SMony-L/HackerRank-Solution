#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
// Using max function()
int max_of_four(int a, int b, int c, int d) {
    int maxAB = max(a,b);
    int maxCD = max(c,d);
    return max(maxAB,maxCD);
}

// Using helper function
// int max_of_two(int a, int b) {
//     return a > b ? a : b;
// }

// int max_of_four(int a, int b, int c, int d) {
//     return max_of_two(max_of_two(a,b), max_of_two(c,d));
// }

// Using two temps
// int max_of_four(int a, int b, int c, int d) {
//     int temp1, temp2;

//     temp1 = a > b ? a : b;
//     temp2 = c > d ? c : d;

//     return temp1 > temp2 ? temp1 : temp2;
// }
int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d\n", ans);
    
    return 0;
}