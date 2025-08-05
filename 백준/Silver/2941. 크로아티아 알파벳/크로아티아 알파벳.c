#include <stdio.h>

int main() {
    char str[101];
    scanf("%s", str);

    int count = 0;
    for (int i = 0; str[i] != '\0'; i++) {

        if (str[i] == 'd' && str[i+1] == 'z' && str[i+2] == '=') {
            count++;
            i += 2;
        }

        else if ((str[i] == 'c' && (str[i+1] == '=' || str[i+1] == '-')) || (str[i] == 'd' && str[i+1] == '-') || (str[i] == 'l' && str[i+1] == 'j') || (str[i] == 'n' && str[i+1] == 'j') || (str[i] == 's' && str[i+1] == '=') || (str[i] == 'z' && str[i+1] == '=')) {
            count++;
            i++;
        }
        else {
            count++;
        }
    }

    printf("%d\n", count);
    return 0;
}
