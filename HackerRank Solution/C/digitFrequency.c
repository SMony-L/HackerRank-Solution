#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char str[1000];
    char map[10];

    scanf("%s", &str);

    for (int i = 0; i < 10; i++) {
        map[i] = 0;
    }
    
    for (int i = 0; i < strlen(str); i++) {
        int x = str[i] - '0';
        if (x >= 0 && x <= 9) {
            map[x]++;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", map[i]);
    }
    printf("\n");
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
