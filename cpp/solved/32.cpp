#include <iostream>
#include <chrono>
#include <vector>
#include "helper/stringfix.h"
#include "helper/largen.h"

using namespace std;

bool process_number(int * pan, Large a) {
    for (int i = 0; i < a.size(); i++) {
        if (pan[a.get(i)] ==  1) {
            return false;
        } else {
            pan[a.get(i)] = 1;
        }
    }
    return true;
}
bool is_pandigital(Large a, Large b, Large c) {
    if ((a.toString()+b.toString()+c.toString()).length() != 9) {
        return false;
    }
    int pan [10];
    int i;
    for (i = 0; i < 10; i++) {
        pan[i] = 0;
    }
    return process_number(pan,a) && process_number(pan,b) && process_number(pan,c) && pan[0] == 0;
}

int solve() {
    int N = 10000, i, s = 0, a, b, c;
    int check [N];
    for (i = 0; i < N; i++) {
        check[i] = 0;
    }
    for (a = 1; a < N; a++) {
        for (b = a; ; b++) {
            c = a*b;
            if ((tostring(a)+tostring(b)+tostring(c)).length() > 9) {
                break;
            }
            if (is_pandigital(Large(a),Large(b),Large(c))) {
                check[c] = 1;
            }
        }
    }
    for (i = 0; i < N; i++) {
        if (check[i] == 1) {
            s += i;
        }
    }
    return s;
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
