#include <iostream>
#include <chrono>
#include <cmath>
#include <vector>
#include <string>
#include "helper/stringfix.h"

using namespace std;


void m(vector<int> * v, int n) {
    int r = 0, s;
    for (int i = v->size()-1; i >= 0; i--) {
        s = v->at(i)*n + r;
        v->operator[](i) = s%10;
        r = s/10;
    }
}

void add(vector<int> * v1, vector<int> * v2) {
    int r = 0, s;
    for (int i = v1->size()-1; i >= 0; i--) {
        s = v1->at(i)+v2->at(i) + r;
        v1->operator[](i) = s%10;
        r = s/10;
    }
}

vector<int> toVector(int n) {
    int tmp = n, i;
    vector<int> v = {0,0,0,0,0,0,0,0,0,0};
    for (i = 9; i >= 0; i--) {
        v[i] = tmp%10;
        tmp = tmp/10;
    }
    return v;
}

string toString(vector<int> * v) {
    string s = "";
    for (int i = 0; i < v->size(); i++) {
        s += itoc(v->at(i));
    }
    return s;
}

string solve() {
    int i, j, N = 1000;
    vector<int> a, tmp;
    a = toVector(0);
    for (i = 1; i <= N; i++) {
        tmp = toVector(1);
        for (j = 0; j < i; j++) {
            m(&tmp,i);
        }
        add(&a,&tmp);
    }
    return toString(&a);
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
