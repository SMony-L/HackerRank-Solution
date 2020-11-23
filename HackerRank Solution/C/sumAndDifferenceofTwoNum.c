#include <stdlib.h>
#include <stdio.h>

int main() {
    int a;
    int b;
    float c;
    float d;
    
    scanf("%d %d %f %f", &a, &b, &c, &d);
    printf("%d %d\n%.1f %.1f\n", a+b, a-b, c+d, c-d);

    return 0;
}