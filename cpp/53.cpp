#include <iostream>
#include <chrono>
#include "helper/largen.h"

using namespace std;

long long f(long long n) {
    long long tmp = 1;
    for (long long i = n; i > 1; i--) {
        tmp = tmp*i;
    }
    return tmp;
}

long long _c(long long n, long long r) {
    return f(n)/(f(r)*f(n-r)); 
}

Large c(long n, long r) {
    Large N (1), D (1);
    long i;
    for (long i = n; i > r; i--) {
        N.multiply(i);
    }
    for (long i = n-r; i > 1; i--) {
        D.multiply(i);
    }
    cout << "N = " << N.toString() << endl;
    cout << "D = " << D.toString() << endl;
    N.divide(D);
    return N; 
}

long f(long n) {
    long tmp = 1, i;
    for (i = n; i > 1; tmp = tmp*i, i--) {}
    return tmp;
}

int solve() {
    cout << _c(5,3) << endl;
    cout << c(5,3).toString() << endl << endl;
    cout << _c(23,10) << endl;
    cout << c(23,10).toString() << endl << endl;
    return 0;
    long n, r;
    int a = 0;
    Large mil (1000000);
    for (n = 1; n <= 24; n++) {
        for (r = 0; r <= n; r++) {
            if (c(n,r).compare(mil) < 0) {
                cout << "FOUND " << n << " " << r << endl;
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
