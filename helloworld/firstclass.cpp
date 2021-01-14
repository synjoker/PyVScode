#include<stdio.h>
int main(){
//     char ch;
//     ch = getchar();
//     putchar(ch);
//     char str[20];
//     printf("\n");
//     gets(str);
//     puts(str);

    char num[20];
    scanf("%[^\n]", &num);
    printf("%s\n", num);
    return 0;
}