#include <iostream>
#include <chrono>
#include <vector>
#include "helper/prime.h"

using namespace std;

int solve() {
    int N = 1000000, r, l, ml = 0, i, j, mp;
    vector<int> s;
    s = sieve(N);
    vector<int> p;
    for (i = 0; i < s.size(); i++) {
        if (s.at(i) == 1) {
            p.push_back(i);
        }
    }
    for (i = 0; i < p.size(); i++) {
        r = 0;
        l = 0;
        for (j = i; j < p.size(); j++) {
            r += p.at(j);
            l++;
            if (r > N) {
                break;
            }
            if (s.at(r) == 1) {
                if (l > ml) {
                    ml = l;
                    mp = r;
                }
            }
        }
    }
    return mp;
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
