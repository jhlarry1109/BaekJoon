#include <stdio.h>

int main() {
    char a[101];
    scanf("%s", a);
    char temp;
    int max;
    for(int i=0; a[i] != '\0'; i++) {
        max = i;
        for(int j=(i+1); a[j] != '\0'; j++) {
            if(a[max] < a[j]) {
                max = j;
            }
        }
        temp = a[i];
        a[i] = a[max];
        a[max] = temp;
    }
    printf("%s", a);
    return 0;
}