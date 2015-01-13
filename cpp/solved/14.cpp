#include <iostream>
#include <vector>
#include <stdexcept>
#include <ctime>

using namespace std;

const int N = 1000000;

long collatz(long n) {
    if (n%2 == 0) {
        return n/2;
    } else {
        return (3*n + 1)/2;
    }
}

int main() {
    time_t start, end;
    time(&start);
    vector<int> v;
    v.resize(N);
    v[1] = 1;
    int i, mi;
    long n;
    int c, mc = 0;
    for (i = 2; i < N; i++) {
        n = i;
        c = 1;
        while (!(n < i)) {
            if (n%2 == 0) {
                n = n/2;
            } else {
                n = (3*n + 1)/2;
            }
            c += 1;
        }
        c = c-1 + v.at((int)n);
        v[i] = c;
        if (c > mc) {
            mi = i;
            mc = c;
        }
    }
    time(&end);
    cout << mi << " with " << mc << endl;
    cout << "Time: " << difftime(end,start) << " sec" << endl;
    return 0;
}
