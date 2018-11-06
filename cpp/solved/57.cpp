#include <iostream>
#include <chrono>
#include "helper/stringfix.h"
#include "helper/largen.h"

using namespace std;

int solve() {
    int j, i, a = 0;
    Large n, d, tmp;
    for (j = 1; j <= 1001; j++) {
        n.reset(1);
        d.reset(2);
        for (i = 0; i < j; i++) {
            tmp.copy(&d);
            d.multiply(2);
            d.add(n);
            n.copy(&tmp);
        }
        n.add(d);
        if (n.size() > d.size()) {
            a++;
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
