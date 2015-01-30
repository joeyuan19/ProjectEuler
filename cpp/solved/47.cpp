#include <iostream>
#include <chrono>
#include <vector>
#include "helper/prime.h"

using namespace std;

int nPrimeFactors(vector<int> * p, int n) {
    int c = 0, t = n, tmp;
    for (int i = 0; i < p->size() && t != 1; i++) {
        if (p->at(i) > n) {
            break;
        } else if (t%p->at(i) == 0) {
            c++;
            while (t%p->at(i) == 0) {
                t = t/p->at(i);
            }
        }
    }
    return c;
}

int solve() {
    int i, j, N = 1000000, L = 4;
    vector<int> p;
    p = primes_up_to(N);
    for (i = 0; i < N-L; i++) {
        for (j = 0; j < L; j++) {
            if (nPrimeFactors(&p,i+j) != L) {
                break;
            }
        }
        if (j == L) {
            break;
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
