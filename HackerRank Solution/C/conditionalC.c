#include <stdio.h>
int main() {

    const char * strings[] = {"one","two","three","four","five","six","seven","eight","nine"};
    int n;
    scanf("%d", &n);
    
    if (n < 1) {
        return 0;
    }
    else if (n >= 1 && n <= 9) {
        printf("%s\n", strings[n-1]);
    } else {
        printf("Greater than 9");
    }

    return 0;
}