#include <iostream>
#include <chrono>
#include <vector>
#include <climits>
#include <cmath>
#include "helper/print.h"

using namespace std;

void sort(vector<long> * v) {
    bool swap = true;
    int i;
    long tmp;
    while (swap) {
        swap = false;
        for (i = 0; i < v->size()-1; i++) {
            if (v->at(i) > v->at(i+1)) {
                tmp = v->at(i);
                v->operator[](i) = v->at(i+1);
                v->operator[](i+1) = tmp;
                swap = true;
            }
        }
    }
}


int find(vector<long> * v, long n, int start, int end) {
    if (n == v->at(start+(end-start)/2)) {
        return start+(end-start)/2;
    } else if (end-start == 1) {
        return -1;
    } else if (n < v->at((end-start)/2)) {
        return find(v,n,start,start+(end-start)/2);
    } else {
        return find(v,n,start+(end-start)/2,end);
    }
}

long find(vector<long> * v, long n) {
    return find(v,n,0,v->size());
}

long pent(long n) {
    return n*(3*n-1)/2;
}

bool isPent(int n) {
    double x = (1. + sqrt(24.*n + 1.))/6.;
    return ((int)x) == x;
}

long solve() {
    long a = 1, b = 1;
    bool found = false;
    for (a = 1; !found; a++) {
        for (b = a-1; b > 0; b--) {
            if (isPent(abs(pent(a)-pent(b))) && isPent(pent(a)+pent(b))) {
                found = true;
                break;
            }
        }
    }
    return pent(a-1)-pent(b);
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
