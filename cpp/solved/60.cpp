#include <iostream>
#include <chrono>
#include <string>
#include <exception>
#include "helper/stringfix.h"
#include "helper/prime.h"

using namespace std;

class Finished: public exception {
    virtual const char* what() const throw() {
        return "Found it!";
    }
} ex;

int concatInts(int a, int b) {
    return stoi(tostring(a)+tostring(b));
}

bool test(int a, int b) {
    return prime(concatInts(a,b)) && prime(concatInts(b,a));
}

bool test(vector<int> * s, int a, int b) {
    int tmp = concatInts(a,b);
    if (tmp > s->size()) {
        if (!prime(tmp)) {
            return false;
        }
    } else {
        if (s->at(tmp) == 0) {
            return false;
        }
    }
    tmp = concatInts(b,a);
    if (tmp > s->size()) {
        if (!prime(tmp)) {
            return false;
        }
    } else {
        if (s->at(tmp) == 0) {
            return false;
        }
    }
    return true;
}

int solve() {
    int a,b,c,d,e;
    int N = 10000;
    int m = 99999;
    vector<int> s;
    s = sieve(99999998);
    for (a = 3; a < N; a += 2) {
        if (s.at(a) == 1) {
            for (b = a-2; b > 2; b -= 2) {
                if (s.at(b) == 1 && test(&s,a,b)) {
                    for (c = b-2; c > 2; c -= 2) {
                        if (s.at(c) == 1 && test(&s,a,b) && test(&s,a,c) && test(&s,b,c)) {
                            for (d = c-2; d > 2; d -= 2) {
                                if (s.at(d) == 1 
                                        && test(&s,a,b) && test(&s,a,c)
                                        && test(&s,a,d) && test(&s,b,c)
                                        && test(&s,b,d) && test(&s,c,d)) {
                                    for (e = d-2; e > 2; e -= 2) {
                                        if (s.at(e) == 1 
                                                && test(&s,a,b) && test(&s,a,c) && test(&s,a,d) && test(&s,a,e)
                                                && test(&s,b,c) && test(&s,b,d) && test(&s,b,e)
                                                && test(&s,c,d) && test(&s,c,e)
                                                && test(&s,d,e)) {
                                                                                        if ((a+b+c+d+e) < m) {
                                                m = (a+b+c+d+e);
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
    return m;
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
