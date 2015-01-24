#include <iostream>
#include <chrono>
#include <vector>
#include "helper/prime.h"
#include "helper/stringfix.h"

using namespace std;

bool pandigital(int r, int n) {
    int pan [r+1];
    int i, tmp;
    for (i = 0; i < r+1; i++) {
        pan[i] = 0;
    }
    tmp = n;
    while (tmp > 0) {
        if (pan[tmp%10] == 1 || pan[tmp%10] > r) {
            return false;
        } else {
            pan[tmp%10] = 1;
        }
        tmp = tmp/10;
    }
    for (i = 1; i < r+1; i++) {
        if (pan[i] == 0) {
            return false;
        }
    }
    return pan[0] == 0;
}

int solve() {
    // 1-9 & 1-8 always divisible by 3
    long N = 10000000, n;
    for (n = N; n >= 0; n--) {
        if (prime(n) && pandigital(tostring(n).length(),n)) {
            break;
        }
    }
    return n;
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
