#include <iostream>
#include <chrono>
#include <vector>
#include "helper/stringfix.h"
#include "helper/largen.h"

using namespace std;

bool is_pandigital(Large a, Large b, Large c) {
    if ((a.toString()+b.toString()+c.toString()).length() != 9) {
        return false;
    }
    int pan [10];
    int i;
    for (i = 0; i < a.size(); i++) {
        if (pan[a.get(i)] == 0) {
            pan[a.get(i)] = 1;
        } else {
            return false;
        }
    }
    for (i = 0; i < b.size(); i++) {
        if (pan[b.get(i)] == 0) {
            pan[b.get(i)] = 1;
        } else {
            return false;
        }
    }
    for (i = 0; i < a.size(); i++) {
        if (pan[b.get(i)] == 0) {
            pan[b.get(i)] = 1;
        } else {
            return false;
        }
    }
    if (pan[0] != 1) {
        return false;
    } else {
        return true;
    }
    return r;
}


int solve() {
    cout << is_pandigital(Large(39),Large(186),Large(7254)) << endl;
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
