#include <iostream>
#include <chrono>
#include <cmath>
#include <vector>
#include "helper/stringfix.h"

using namespace std;

vector<int> reduce(vector<int> * a, int a_idx, vector<int> * b, int b_idx) {
    vector<int> tmp (2,0);
    int _a = 1, _b = 1, i;
    for (i = a->size()-1; i >= 0; i--) {
        if (i != a_idx) {
            tmp[0] += a->at(i)*_a;
            _a = _a*10;
        }
    }
    for (i = b->size()-1; i >= 0; i--) {
        if (i != b_idx) {
            tmp[1] += b->at(i)*_b;
            _b = _b*10;
        }
    }
    return tmp;
}


vector<vector<int>> foolish_reductions(int a, int b) {
    vector<int> A, B;
    vector<vector<int>> r;
    int tmp = a;
    while (tmp > 0) {
        A.insert(A.begin(),tmp%10);
        tmp = tmp/10;
    }
    tmp = b;
    while (tmp > 0) {
        B.insert(B.begin(),tmp%10);
        tmp = tmp/10;
    }
    int i, j;
    for (i = 0; i < A.size(); i++) {
        for (j = 0; j < B.size(); j++) {
            if (A.at(i) == B.at(j) && A.at(i) != 0) {
                r.push_back(reduce(&A,i,&B,j));
            }
        }
    }
    return r;
}

bool condition(int a, int b) {
    vector<vector<int>> reductions;
    reductions = foolish_reductions(a,b);
    for (int i = 0; i < reductions.size(); i++) {
        if (((double)a)/b == ((double)reductions.at(i)[0])/reductions.at(i)[1]) {
            return true;
        }
    }
    return false;
}

int solve() {
    int n, d, i;
    int N = 1, D = 1;
    for (d = 10; d <= 99; d++) {
        for (n = 10; n <= d-1; n++) {
            if (condition(n,d)) {
                D = D*d;
                N = N*n;
            }
        }
    }
    bool reduced = true;
    while (reduced) {
        reduced = false;
        for (i = min(N,D); i > 1; i++) {
            if (N%i == 0 && D%i == 0) {
                N = N/i;
                D = D/i;
                reduced = true;
                break;
            }
        }
    }
    return D;
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
