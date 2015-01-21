#include <iostream>
#include <chrono>
#include "helper/prime.h"

using namespace std;

vector<int> toVector(int i) {
    vector<int> v;
    if (i == 0) {
        v.push_back(0);
    } else {
        int tmp = i;
        while (tmp > 0) {
            v.insert(v.begin(),tmp%10);
            tmp = tmp/10;
        }
    }
    return v;
}

int toInt(vector<int> * v) {
    int s = 0, tmp = 1, i;
    for (i = v->size()-1; i >= 0; i--) {
        s += v->at(i)*tmp;
        tmp = tmp*10;
    }
    return s;
}

void rotate(vector<int> * v) {
    int tmp = v->at(0), i;
    for (i = 0; i < v->size()-1; i++) {
        v->operator[](i) = v->at(i+1);
    }
    v->operator[](i) = tmp;
}

int solve() {
    int N = 1000000, i, j, a = 0;
    bool isCircular = true;
    vector<int> s;
    s = sieve(N);
    for (int i = 1; i < N; i++) {
        vector<int> n;
        n = toVector(i);
        isCircular = true;
        for (j = 0; j < n.size(); j++) {
            if (n.at(0) != 0 && s[toInt(&n)] != 1) {
                isCircular = false;
                break;
            }
            rotate(&n);
        }
        if (isCircular) {
            a += 1;
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
