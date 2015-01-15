#include <iostream>
#include <ctime>
#include <vector>
#include "helper/largen.h"


using namespace std;

int solve() {
    int L = 2000, N = 1000;
    Large a (L,1);
    Large b (L,1);
    Large c;
    int n = 2;
    while (b.toString().length() < N) {
        c.copy(&b);
        b.add(a);
        a.copy(&c);
        n++;
    }
    return n;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << " s" << endl;
    return 0;
}
