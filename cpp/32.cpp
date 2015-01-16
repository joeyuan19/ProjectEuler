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
}


int solve() {
    
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
