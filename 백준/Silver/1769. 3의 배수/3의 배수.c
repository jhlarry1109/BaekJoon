#include <stdio.h>
#include <string.h>

int main() {
    char a[1000001];
    int y;
    int cnt = 0;
    scanf("%s", a);
    while (strlen(a) > 1) {
        y = 0;
        cnt++;
        for(int i=0; a[i] != '\0'; i++) {
            y += a[i]-'0';
        }
        sprintf(a, "%d", y);
    }
    printf("%d\n", cnt);
    if (a[0]=='9' || a[0]=='6' || a[0]=='3') {
        printf("YES");
    }
    else{
        printf("NO");
    }
    return 0;
}