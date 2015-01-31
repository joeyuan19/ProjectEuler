#include <iostream>
#include <chrono>
#include "helper/prime.h"
#include "helper/stringfix.h"

using namespace std;

void bubbleSort(vector<int> * v) {
    bool swap = true;
    int tmp, i;
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

void sort(vector<int> * v) {
    bubbleSort(v);
}

void p(vector<int> * v) {
    cout << "Vector of size: " << v->size() << endl;
    for (int i = 0; i < v->size(); i++) {
        cout << v->at(i) << ", ";
    }
    cout << endl;
}

vector<int> toVector(int n) {
    if (n == 0) {
        vector<int> v;
        v.push_back(0);
        return v;
    }
    int tmp = n;
    vector<int> v;
    while (tmp > 0) {
        v.insert(v.begin(),tmp%10);
        tmp = tmp/10;
    }
    return v;
}

bool permutation(int a, int b) {
    vector<int> A;
    A = toVector(a);
    sort(&A);
    vector<int> B;
    B = toVector(b);
    sort(&B);
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

string solve() {
    int n, d, i, N = 10000;
    bool found = true;
    for (n = N/10+488; n < N; n++) {
        if (prime(n)) {
            for (d = 1; 2*d+n < N; d++) {
                found = true;
                for (i = 1; i < 3; i++) {
                    if (!prime(n+i*d) || !permutation(n,n+i*d)) {
                        found = false;
                        break;
                    }
                }
                if (found) {
                    break;
                }
            }
            if (found) {
                break;
            }
        }
    }
    return tostring(n)+tostring(n+d)+tostring(n+2*d);
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
