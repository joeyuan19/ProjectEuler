#include <iostream>
#include <chrono>
#include <vector>
#include "helper/largen.h"

using namespace std;

int solve() {
    int i;
    vector<int> v = {1}, t = {1};
    for (i = 1; i <= 100; i++) {
        v.push_back(1);
        v.push_back(i*2);
        v.push_back(1);
        t.push_back(2);
        t.push_back(2);
        t.push_back(2);
    }
    int c = 99;
    Large n, d, tmp;
    n.reset(1);
    d.reset(v.at(c));
    for (i = c-1; i > 0; i--) {
        tmp.copy(&d);
        d.multiply(v.at(i));
        d.add(n);
        n.copy(&tmp);
    }
    tmp.copy(&d);
    tmp.multiply(2);
    n.add(tmp);
    int a = 0;
    for (int i = 0; i < n.size(); i++) {
        a += n.get(i);
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
