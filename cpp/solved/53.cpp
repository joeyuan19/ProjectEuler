#include <iostream>
#include <chrono>
#include "helper/largen.h"

using namespace std;

bool condition(long n, long r) {
    Large N (1), D (1);
    long i;
    for (i = n; i > r; i--) {
        N.multiply(i);
    }
    for (i = n-r; i > 1; i--) {
        D.multiply(i);
    }
    if (N.size()-D.size() >= 7) {
        return true;
    } else if (N.size()-D.size() == 6) {
        N.divide(D);
        Large mill (1000000);
        return N.compare(mill) > 0;
    } else {
        return false;
    }
}

int solve() {
    long n, r;
    int a = 0;
    for (n = 1; n <= 100; n++) {
        for (r = 0; r <= n; r++) {
            if (condition(n,r)) {
                a++;
            }
        }
    }
    return a;
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
