#include <iostream>
#include <chrono>
#include <cmath>

using namespace std;

bool isTri(long x) {
    double n = (sqrt(8*x + 1) - 1)/2;
    return ((long)n) == n;
}

bool isPent(long x) {
    double n = (sqrt(24*x + 1) + 1)/6;
    return ((long)n) == n;
}

bool isHex(long x) {
    double n = (sqrt(8*x + 1) + 1)/4;
    return ((long)n) == n;
}

long solve() {
    long i = 40755;
    i++;
    while (true) {
        if (isTri(i) && isPent(i) && isHex(i)) {
            break;
        }
        i++;
    }
    return i;
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
