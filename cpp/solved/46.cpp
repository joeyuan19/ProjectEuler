#include <iostream>
#include <chrono>
#include <vector>
#include "helper/prime.h"


using namespace std;

int solve() {
    int N = 100000;
    vector<int> s;
    s = sieve(N);
    int i, j;
    bool found = true;
    for (i = 3; i < N; i += 2) {
        if (s[i] == 0) {
            found = false;
            for (j = 0; j < i; j++) {
                if (i - 2*j*j < 0) {
                    break;
                } else if (s[i-(2*j*j)] == 1) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                break;
            }
        }
    }
    return i;
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
