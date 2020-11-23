#include <stdio.h>
void update(int *a, int* b) {
    int temp = *a;
    *a = *a + *b;  
    *b = abs(*b - temp);

    // method without using another variable to temp store variable a
    // a value has been changed so a - b will not be correct
    // substract b 2 times will solve the problem
    // *a = *a + *b;
    // *b = abs (*a - (2**b));

}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;

    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d\n", a,b);

    return 0;
}