#include <stdio.h>

int main() {
    int n;
    char a[101];
    int cnt = 0;
    int be;
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        int group = 1;
        int li[26] = {0};
        scanf("%s", a);
        be = 0;
        for(int j=0; a[j] != '\0'; j++) {
            if (li[a[j] - 'a'] == 1 && be != a[j]) {
                group = 0;
                break;
            }
            be = a[j];
            li[a[j] - 'a'] = 1;
        }
        if(group) {
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}