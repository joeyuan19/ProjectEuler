#include <iostream>
#include <chrono>
#include <string>
#include "helper/stringfix.h"

using namespace std;

bool pandigital(string s) {
    int pan [10];
    int i;
    for (i = 0; i < 10; i++) {
        pan[i] = 0;
    }
    for (i = 0; i < s.length(); i++) {
        if (pan[ctoi(s[i])] == 1) {
            return false;
        } else {
            pan[ctoi(s[i])] = 1;
        }
    }
    for (i = 1; i < 10; i++) {
        if (pan[i] == 0) {
            return false;
        }
    }
    return pan[0] == 0;
}

int solve() {
    int n, N = 10000;
    int i;
    long a, ma = 0;
    string s = "";
    for (n = 1; n < N; n++) {
        s = "";
        for (i = 1; i < 100; i++) {
            s += tostring(n*i);
            if (s.length() > 9) {
                break;
            } else if (pandigital(s)) {
                a = stol(s);
                if (a > ma) {
                    ma = a;
                }
                break;
            }
        }
    }
    return ma;
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
