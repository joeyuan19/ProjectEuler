#include <iostream>
#include <chrono>
#include <cmath>
#include "helper/largen.h"

using namespace std;

int find(vector<string> * v, string s) {
    for (int i = 0; i < v->size(); i++) {
        if (v->at(i).compare(s) == 0) {
            return i;
        }
    }
    return -1;
}

int solve() {
    vector<string> v;
    string s;
    int i, a, b, N = 100;
    for (a = 2; a <= N; a++) {
        for (b = 2; b <= N; b++) {
            Large n (210,1);
            for (i = 0; i < b; i++) {
                n.multiply(a);
            }
            s = n.toString();
            if (find(&v,s) < 0) {
                v.push_back(s);
            }
        }
    }
    return v.size();
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
