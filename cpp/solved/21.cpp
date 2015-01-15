#include <iostream>
#include <ctime>
#include <vector>
#include "helper/prime.h"

using namespace std;

void print(vector<int> *v);

class Index {
    public:
        Index(vector<int>);
        vector<int> indices;
        vector<int> limits;
        void reset() {
            for (int i = 0; i < indices.size(); i++) {
                indices[i] = 0;
            }
        };
        bool finished() {
            for (int i = 0; i < indices.size(); i++) {
                if (indices[i] != limits[i]) {
                    return false;
                }
            }
            return true;
        };
        bool next() {
            for (int i = 0; i < indices.size(); i++) {
                if (indices.at(i) == limits.at(i)) {
                    while (i < indices.size() && indices.at(i) == limits.at(i)) {
                        i++;
                    }
                    if (i == indices.size()) {
                        return false;
                    } else {
                        indices[i] += 1;
                        for (int j = 0; j < i; j++) {
                            indices[j] = 0;
                        }
                        return true;
                    }
                } else {
                    indices[i] += 1;
                    return true;
                }
            }
        }
};

Index::Index(vector<int> lims) {
    indices.resize(lims.size());
    limits.resize(lims.size());
    for (int i = 0; i < lims.size(); i++) {
        limits[i] = lims[i];
        indices[i] = 0;
    }
}

int pow(int a, int b) {
    int p = 1;
    for (int i = 0; i < b; i++) {
        p = p*a;
    }
    return p;
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

void print(vector<int> * v) {
    for (int i = 0; i < v->size(); i++) {
        cout << v->at(i);
        if (i != v->size()-1) {
            cout << ", ";
        }
    }
    cout << endl;
}

int solve() {
    int N = 10000, i, j, a = 0;
    vector<int> p;
    p = primes_up_to(N);
    vector<int> d;
    d.push_back(0);
    for (i = 1; i < N; i++) {
        d.push_back(divs(&p,i));
        if (d.at(i) < i && d.at(d.at(i)) == i) {
            a += i+d.at(i);
        }
    }
    return a;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
