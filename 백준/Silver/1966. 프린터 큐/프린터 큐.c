#include <stdio.h>

int front;
int rear;


int main() {
    int t, n, m;
    scanf("%d", &t);
    for(int i=0; i<t; i++) {
        int li[1001] = {0};
        int idx[1001] = {0};
        scanf("%d %d", &n, &m);
        front = 0;
        rear = n;
        for(int j=0; j<n; j++) {
            scanf("%d", &li[j]);
            idx[j] = j;
        }

        int ord = 0;
        
        while (front < rear) {
            int value = li[front];
            int index = idx[front];
            int new = 0;
            for(int j=front+1; j<rear; j++) {
                if (li[j] > value) {
                    new = 1;
                    break;
                }
            }
            if (new) {
                li[rear] = value;
                idx[rear] = index;
                rear++;
                front++;
            }
            else {
                ord++;
                if(index == m) {
                    printf("%d\n", ord);
                    break;
                }
                front++;
            }
        }
    }
    return 0;
}