#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    //Write your logic to print the tokens of the sentence here.

    for (char *c = s; *c != '\0'; c++) {
        if (*c == ' ') {
            *c = '\n';
        }
    }
    printf("%s\n", s);
    
    // Another method of doing it
    // for(int i = 0; i < strlen(s) ; i++)
    // {  
    //     if(s[i] == ' ')
    //         printf("\n");
    //     else
    //         printf("%c",s[i]);
    // }    
    free(s);
    return 0;
}