#include <iostream>
#include <chrono>
#include <vector>
#include "helper/prime.h"
#include "helper/stringfix.h"

using namespace std;

vector<int> toVector(int n) {
    if (n == 0) {
        return (vector<int> (1,0));
    }
    int tmp = n;
    vector<int> v;
    while (tmp > 0) {
        v.insert(v.begin(),tmp%10);
        tmp = tmp/10;
    }
    return v;
}

int toInt(vector<int> * v) {
    int t = 1, n = 0;
    for (int i = v->size()-1; i >= 0; i--) {
        n += t*v->at(i);
        t = t*10;
    }
    return n;
}

void p(vector<int> * v) {
    for (int i = 0; i < v->size(); i++) {
        cout << v->at(i);
        if (i < v->size()-1) {
            cout << ", ";
        }
    }
    cout << endl;
}

void replace(vector<int> * v, int repl, int with) {
    if (with == 0 && v->at(0) == repl) {
        return;
    }
    for (int i = 0; i < v->size(); i++) {
        if (v->at(i) == repl) {
            v->operator[](i) = with;
        }
    }
}

int replace(int n, int repl, int with) {
    vector<int> v;
    v = toVector(n);
    replace(&v,repl,with);
    return toInt(&v);
}

int solve() {
    int target = 8, count;
    int i, j, k, r;
    bool found = false;
    for (i = 1; ; i++) {
        if (prime(i)) {
            for (j = 0; j < 10; j++) {
                count = 1;
                found = false;
                for (k = 0; k < 10; k++) {
                    if (j != k) {
                        r = replace(i,j,k);
                        if (r == i) {
                        } else if (prime(r)) {
                            count++;
                        }
                    }
                }
                cout << i << " " << j << " " << count << endl << endl;
                if (count >= target) {
                    found = true;
                    break;
                }
            }
            if (found) {
                cout << i << endl;
                break;
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
