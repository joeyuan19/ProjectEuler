#include <iostream>

using namespace std;

int rule(int a, int b, int c) {
    if (a*a + b*b == c*c) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int a, b, c, N = 1000;
    for (a = 1; a < N; a++) {
        for (b = a; b < N; b++) {
            for (c = b; c < N; c++) {
                if (rule(a,b,c) == 1 && a+b+c == N) {
                    cout << a << "," << b << "," << c << endl;
                    cout << a*b*c << endl;
                }
            }
        }
    }
    return 0;
}
