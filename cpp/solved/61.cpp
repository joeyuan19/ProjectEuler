#include <iostream>
#include <chrono>
#include <vector>
#include "helper/stringfix.h"
#include "helper/geonums.h"

using namespace std;

class Finished: public exception {
    virtual const char* what() const throw() {
        return "Found it!";
    }
} ex;

bool test(vector<int> * set) {
    return false;
}

bool isCyclicSet(vector<int> * set) {
    for (int i = 0; i < set->size(); i++) {
        if (tostring(set->at(i)).substr(2,2).compare(tostring(set->at((i+1)%set->size())).substr(0,2)) != 0) {
            return false;
        }
    }
    return true;
}

int sumVector(vector<int> * v) {
    int s = 0;
    for (int i = 0; i < v->size(); i++) {
        s += v->at(i);
    }
    return s;
}

void printVector(vector<int> * v) {
    for (int i = 0; i < v->size(); i++) {
        cout << v->at(i) << " ";
    }
    cout << endl;
}


int concat(int a, int b) {
    return stoi(tostring(a)+tostring(b));
}

bool condition(vector<int> * v) {
    int t, s, p, hx, hp, o;
    for (t = 0; t < v->size(); t++) {
        if (isTriangular(v->at(t))) {
            for (s = 0; s < v->size(); s++) {
                if (s != t && isSquare(v->at(s))) {
                    for (p = 0; p < v->size(); p++) {
                        if (p != t && p != s && isPentagonal(v->at(p))) {
                            for (hx = 0; hx < v->size(); hx++) {
                                if (hx != t && hx != s && hx != p && isHexagonal(v->at(hx))) {
                                    for (hp = 0; hp < v->size(); hp++) {
                                        if (hp != t && hp != s && hp != p && hp != hx && isHeptagonal(v->at(hp))) {
                                            for (o = 0; o < v->size(); o++) {
                                                if (o != t && o != s && o != p && o != hx && o != hp && isOctagonal(v->at(o))) {
                                                    return true;
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}

bool chains(int a, int b) {
    return tostring(a).substr(2,2).compare(tostring(b).substr(0,2)) == 0;
}


int solve() {
    vector<int> t, s, p, hx, hp, o, v;
    int i, tmp = 0;
    for (i = 0; i < 150; i++) {
        tmp = octagon(i);
        if (10000 > tmp && tmp > 1000) {
            o.push_back(tmp);
        }
        tmp = heptagon(i);
        if (10000 > tmp && tmp > 1000) {
            hp.push_back(tmp);
        }
        tmp = hexagon(i);
        if (10000 > tmp && tmp > 1000) {
            hx.push_back(tmp);
        }
        tmp = pentagon(i);
        if (10000 > tmp && tmp > 1000) {
            p.push_back(tmp);
        }
        tmp = square(i);
        if (10000 > tmp && tmp > 1000) {
            s.push_back(tmp);
        }
        tmp = triangle(i);
        if (10000 > tmp && tmp > 1000) {
            t.push_back(tmp);
        }
    }
    int a,b,c,d,e,f;
    int A,B,C,D,E,F;
    int j,k,l,m;
    vector<vector<int>> nums = {t,s,p,hx,hp,o};
    v = {0,0,0,0,0,0};
    try {
        for (a = 0; a < nums.at(0).size(); a++) {
            A = nums.at(0).at(a);
            for (b = 1; b < nums.size(); b++) {
                for (i = 0; i < nums.at(b).size(); i++) {
                    B = nums.at(b).at(i);
                    if (chains(A,B)) {
                        for (c = 1; c < nums.size(); c++) {
                            if (c != b) {
                                for (j = 0; j < nums.at(c).size(); j++) {
                                    C = nums.at(c).at(j);
                                    if (chains(B,C)) {
                                        for (d = 1; d < nums.size(); d++) {
                                            if (d != b && d != c) {
                                                for (k = 0; k < nums.at(d).size(); k++) {
                                                    D = nums.at(d).at(k);
                                                    if (chains(C,D)) {
                                                        for (e = 1; e < nums.size(); e++) {
                                                            if (e != b && e != c && e != d) {
                                                                for (l = 0; l < nums.at(e).size(); l++) {
                                                                    E = nums.at(e).at(l);
                                                                    if (chains(D,E)) {
                                                                        for (f = 1; f < nums.size(); f++) {
                                                                            if (f != b && f != c && f != d && f != e) {
                                                                                for (m = 0; m < nums.at(f).size(); m++) {
                                                                                    F = nums.at(f).at(m);
                                                                                    if (chains(E,F) && chains(F,A)) {
                                                                                        v = {A,B,C,D,E,F};
                                                                                        throw ex;
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    } catch (exception& e) {
    }
    printVector(&v);
    return sumVector(&v);
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
