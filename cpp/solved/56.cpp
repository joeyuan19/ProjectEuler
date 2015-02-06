#include <iostream>
#include <chrono>
#include <vector>
#include "helper/largen.h"

using namespace std;

int digitSum(vector<int> * v) {
    int s = 0;
    for (int i = 0; i < v->size(); i++) {
        s += v->at(i);
    }
    return s;
}

int solve() {
    int a,b;
    int m = 0, d;
    vector<int> num;
    Large n;
    for (a = 1; a < 100; a++) {
        n.reset(a);
        for (b = 1; b < 100; b++) {
            num = n.getNumber();
            d = digitSum(&num);
            if (d > m) {
                m = d;
            }
            n.multiply(a);
        }
    }
    return m;
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
