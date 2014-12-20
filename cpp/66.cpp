#include <iostream>
#include <tgmath.h>
#include <cmath>

using namespace std;

int period(double n) {
    double a0 = floor(n);
    int s = 0;
    while (floor(n) != 2*a0) {
        n = 1/(n-floor(n));
        s += 1;
    }
    return s;
}

int main() {
    int N = 10000;
    int s = 0;
    int tmp;
    for (double i = 2; i < N+1; i += 1) {
        if (floor(sqrt(i)) == sqrt(i)) {
            continue;
        }
        tmp = period(sqrt(i));
        if (tmp%2 == 1) {
            s += 1;
        }
    }
    cout << s << endl;
    return 1;
}



