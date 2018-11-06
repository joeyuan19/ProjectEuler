#include <iostream>
#include <chrono>
#include <cmath>
#include "helper/prime.h"

using namespace std;

int solve() {
    int n, s = 3, i, N = 7;
    double p = 0.0;
    for (n = 2, i = 1; ; n++, i++) {
        if (i%(s-1) == 0 && prime(n)) {
            p += 1.0;
        }
        //cout << "n = " << n << " i = " << i << " p = " << p << " s = " << s << " r = " << p << "/" << (2*s-1) << " = " << p/(2*s-1) << endl;
        if (n%2 == 1 && sqrt(n) == ((int)sqrt(n))) {
            if (p/(2*s+1) < .1) {
                break;
            }
            i = 0;
            s += 2;
        }
    }
    return s;
}

int main() {
    typedef chrono::high_resolution_clock Clock;
    typedef chrono::milliseconds milliseconds;
    Clock::time_point start = Clock::now();
    cout << "Answer: " << solve() << endl;
    Clock::time_point end = Clock::now();
    milliseconds ms = chrono::duration_cast<milliseconds>(end-start);
    cout << "Time: " << ms.count() << " ms" << endl;
    return 0;
}
