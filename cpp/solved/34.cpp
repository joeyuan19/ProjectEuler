#include <iostream>
#include <chrono>
#include "helper/largen.h"

using namespace std;

long factorial(long n) {
    long tmp = n, p = 1;
    while (tmp > 1) {
        p = p*tmp;
        tmp = tmp - 1;
    }
    return p;
}

long solve() {
    int i, j, N = 10000000;
    long a = 0, s;
    bool start;
    for (i = 10; i < N; i++) {
        Large n (i);
        s = 0;
        start = false;
        for (j = 0; j < n.size(); j++) {
            if (start) {
                s += factorial(n.get(j));
            } else if (n.get(i) != 0) {
                s += factorial(n.get(j));
                start = false;
            }
        }
        if (i == s) {
            a += n.toLong();
        } else if (s > i) {
            i = i+10 - (i+10)%10 -1;
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
