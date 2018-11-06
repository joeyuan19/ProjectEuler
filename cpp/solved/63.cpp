#include <iostream>
#include <chrono>
#include "helper/largen.h"

using namespace std;

int solve() {
    Large tmp;
    int i, n, N = 8, a = 1;
    for (i = 2, tmp.reset(i); i < 10; i++, tmp.reset(i)) {
        for (n = 1; tmp.size() >= n; n++) {
            if (tmp.size() == n) {
                a++;
            }
            tmp.multiply(i);
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
