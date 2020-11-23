#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch;
    char s[50];
    char sen[50];
    
    scanf("%c%*c", &ch);
    scanf("%s%*c", &s);
    scanf("%[^\n]%*c", &sen);
    
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);
    
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}