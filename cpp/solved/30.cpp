#include <iostream>
#include <chrono>
#include "helper/largen.h"
#include <cmath>
#include <string>

using namespace std;

const int P = 5;

int f(Large n) {
    int s = 0, i;
    for (i = 0; i < n.size(); i++) {
        s += pow(n.get(i),P);
    }
    return s;
}


string solve() {
    long i, N = 10000000;
    Large a, b;
    for (i = 10; i < N; i++) {
        Large n (10,i);
        if (n.compare(Large(f(n))) == 0) {
            a.add(n);
        }
    }
    return a.toString();
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
