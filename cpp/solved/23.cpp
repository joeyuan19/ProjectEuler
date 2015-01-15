#include <iostream>
#include <ctime>
#include <cmath>
#include "helper/prime.h"
#include "helper/index.h"

using namespace std;

void print(vector<int> * v) {
    int i;
    for (i = 0; i < v->size()-1; i++) {
        cout << v->at(i) << ", ";
    }
    cout << v->at(i) << endl;
}

void sort_and_remove_duplicates(vector<int> * v) {
    int tmp, i;
    bool swapMade = true;
    while (swapMade) {
        swapMade = false;
        for (i = 0; i < v->size()-1; i++) {
            if (v->at(i) > v->at(i+1)) {
                tmp = v->at(i);
                v->operator[](i) = v->at(i+1);
                v->operator[](i+1) = tmp;
                swapMade = true;
            } else if (v->at(i) == v->at(i+1)) {
                v->erase(v->begin()+i+1);
                swapMade = true;
            }
        }
        print(v);
    }
}

int divs(vector<int> * primes, int n) {
    int i, p, e, tmp;
    vector<int> divs; 
    vector<int> exps;
    for (i = 0; i < primes->size(); i++) {
        p = primes->at(i);
        if (p*2 > n) {
            break;
        } else {
            if (n%p == 0) {
                tmp = p;
                e = 1;
                while (n%tmp == 0) {
                    tmp = tmp*p;
                    e++;
                }
                e--;
                divs.push_back(p);
                exps.push_back(e);
            }
        }
    }
    int s = 0, j;
    Index idx (exps);
    vector<int> divisors;
    while (true) {
        tmp = 1;
        for (i = 0; i < idx.indices.size(); i++) {
            tmp = tmp*pow(divs[i],idx.indices[i]);
        }
        if (tmp < n) {
            s += tmp;
        }
        if (!idx.next()) {
            break;
        }
    }
    return s;
}

void insert_sorted(vector<int> * v, int value) {
    int i;
    for (i = 0; i < v->size(); i++) {
        if (v->at(i) > value) {
            v->insert(v->begin()+i,value);
            return;
        } else if (v->at(i) == value) {
            return;
        }
    }
    v->insert(v->begin()+i,value);
    return;
}

long solve() {
    int n, N = 28123;
    int i, s;
    long a = 0;
    vector<int> abundant;
    vector<int> sums (N+1,0);
    vector<int> p;
    p = primes_up_to(N);
    for (n = 1; n <= N; n++) {
        if (n < divs(&p,n)) {
            abundant.push_back(n);
            for (i = 0; i < abundant.size(); i++) {
                s = n + abundant.at(i);
                if (s > N) {
                    break;
                } else {
                    sums[s] = 1;
                }
            }
        }
    }
    for (i = 0; i <= N; i++) {
        if (sums[i] == 0) {
            a += i;
        }
    }
    cout << a - 4179871 << endl;
    return a;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << " s" << endl;
    return 0;
}
