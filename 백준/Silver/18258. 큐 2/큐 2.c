#include <stdio.h>

int queue[2000000];
int front = -1;
int rear = -1;

int push(int n) {
    rear++;
    queue[rear] = n;
}

int empty() {
    if (front == rear) {
        return 1;
    }
    else {
        return 0;
    }
}

int pop() {
    if (empty()) {
        return -1;
    }
    front++;
    return queue[front];
}

int size() {
    return rear - front;
}

int fr() {
    if(empty()) {
        return -1;
    }
    else {
        return queue[front+1];
    }
}

int back() {
    if(empty()) {
        return -1;
    }
    else {
        return queue[rear];
    }
}

int main() {
    int n;
    int x;
    char a[10];
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%s", a);
        if (a[0] == 'p' && a[1] == 'u') {
            scanf("%d", &x);
            push(x);
        }
        else if (a[0] == 'p' && a[1] == 'o') {
            printf("%d\n", pop());
        }
        else if (a[0] == 's' && a[1] == 'i') {
            printf("%d\n", size());
        }
        else if (a[0] == 'e' && a[1] == 'm') {
            printf("%d\n", empty());
        }
        else if (a[0] == 'f' && a[1] == 'r') {
            printf("%d\n", fr());
        }
        else if (a[0] == 'b' && a[1] == 'a') {
            printf("%d\n", back());
        }
    }
    return 0;
}
