#include <iostream>
#include <chrono>
#include "helper/prime.h"

using namespace std;

int solve() {
    int n, s = 1, i = 0;
    double p = 0.0;
    for (n = 1; s <= 6 ; n++, i++) {
        if (i%s == 0) {
            if (prime(n)) {
                cout << "prime n = " << n << endl;
                p += 1.0;
                if (p/(2*s+1) < .1) {
                    break;
                }
            }
        }
        if (i/s == 4) {
            cout << (p/n) << " side: " << s << endl;
            i = 0;
            s += 2;
        }
    }
    return s+1;
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
