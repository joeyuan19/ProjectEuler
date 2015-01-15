#include <iostream>
#include <ctime>
#include <string>
#include <vector>
#include "helper/tostring.h"

using namespace std;


void m(vector<int> * v, int n) {
    int i, tmp = 0;
    for (i = v->size()-1; i >= 0; i--) {
        tmp = v->at(i)*n + tmp;
        v->operator[](i) = tmp%10;
        tmp = tmp/10;
    }
}

string p(vector<int> * v) {
    int i;
    bool print = false;
    string s = "";
    for (i = 0; i < v->size(); i++) {
        if (v->at(i) != 0) {
            print = true;
        }
        if (print) {
            s += tostring(v->at(i));
        }
    }
    return s;
}

long solve() {
    int N = 999, L = 1000, i;
    vector<int> v (L,0);
    v[L-1] = 2;
    for (i = 0; i < N; i++) {
        m(&v,2);
    }
    cout << p(&v) << endl;
    long s = 0;
    for (i = 0; i < L; i++) {
        s += v.at(i);
    }
    return s;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
