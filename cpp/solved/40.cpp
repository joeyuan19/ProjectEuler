#include <iostream>
#include <chrono>
#include <string>
#include "helper/stringfix.h"

using namespace std;

int solve() {
    string d = ".";
    int i = 1, N = 1000000;
    while (d.length() <= N) {
        d += tostring(i);
        i++;
    }
    long a = 1;
    a = a*ctol(d[1]);
    cout << d[1] << endl;
    a = a*ctol(d[10]);
    cout << d[10] << endl;
    a = a*ctol(d[100]);
    cout << d[100] << endl;
    a = a*ctol(d[1000]);
    cout << d[1000] << endl;
    a = a*ctol(d[10000]);
    cout << d[10000] << endl;
    a = a*ctol(d[100000]);
    cout << d[100000] << endl;
    a = a*ctol(d[1000000]);
    cout << d[1000000] << endl;
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
