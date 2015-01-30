#include <iostream>
#include <chrono>
#include "helper/prime.h"

using namespace std;

void bubbleSort(vector<int> * v) {
    bool swap = true;
    while (swap) {
        swap = false;
        for (int i = 0; i < v->size()-1; i++) {
            if (v->at(i) > v->at(i+1)) {
                tmp = v->at(i);
                v->operator[](i) = v->at(i+1);
                v->operator[](i+1) = tmp;
                swap = true;
            }
        }
    }
}

void sort(vector<int> * v) {
    bubbleSort(v,0,v->size());
}

vector<int> toVector(int n) {
    int tmp = n;
    vector<int> v;
    while (tmp > 0) {
        v.insert(v.begin(),tmp%10);
        tmp = tmp/10;
    }
}

bool permutation(int a, int b) {
    vector A, B;
    A = toVector(a);
    sort(A);
    B = toVector(b);
    sort(B);
    if (A.size() != B.size()) {
        return false;
    } else {
        for (int i = 0; i < A.size(); i++) {
            if (A.at(i) != B.at(i)) {
                return false;
            }
        }
        return true;
    }
}

int solve() {
    int n, d, i, N = 10000;
    for (n = 0; n < N; n++) {
        if (prime(n)) {
            for (d = 1; 2*d+n < N; d++) {
                for (i = 1; i < 3; i++) {
                    if (!prime(n+i*d) || !permutation(n,n+i*d)) {
                        break;
                    }
                }
                if (j == 3) {
                    break;
                }
            }
        }
    }
    return 0;
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
