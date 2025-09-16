import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int l = input.nextInt();
        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();
        int d = input.nextInt();
        int math = (a+c-1) / c;
        int kor = (b+d-1) / d;
        int max = (math > kor) ? math : kor;
        System.out.println(l-max);
    }
}