#include <iostream>
#include <chrono>

using namespace std;

bool isRightTriangle(int a, int b, int c) {
    return c*c == a*a + b*b;
}

int solve() {
    int p, P = 1000;
    int a, b, c;
    int m = 0, s;
    int mp;
    for (p = 3; p <= P; p++) {
        s = 0;
        for (a = 1; a < p; a++) {
            for (b = a; b < p; b++) {
                c = p-a-b;
                if (c > 0 && isRightTriangle(a,b,c)) {
                    s++;
                }
            }
        }
        if (s > m) {
            m = s;
            mp = p;
        }
    }
    return mp;
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
