#include <iostream>
#include <chrono>
#include "helper/prime.h"

using namespace std;

bool condition(vector<int> * s, long n) {
    if (s->at(n) != 1) {
        return false;
    }
    long tmp = 10;
    while (n/tmp > 0) {
        if (s->at(n/tmp) != 1 || s->at(n%tmp) != 1) {
            return false;
        }
        tmp = tmp*10;
    }
    return true;
}

long solve() {
    long N = 10000000, count = 0, a = 0;
    vector<int> s;
    s = sieve(N);
    for (long i = 11; ; i += 2) {
        if (condition(&s,i)) {
            a += i;
            count++;
        }
        if (count == 11) {
            break;
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
