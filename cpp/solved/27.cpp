#include <iostream>
#include <ctime>
#include "helper/prime.h"

using namespace std;

int run(int a, int b) {
    int n = 0;
    while (prime(n*n + a*n + b)) {
        n++;
    }
    return n;
}

int solve() {
    int a, b, N = 1000, r, mr = 0, answer = 0;
    vector<int> p;
    p = primes_up_to(N);
    for (b = 0; b < p.size(); b++) {
        for (a = -(N-1); a < N; a++) {
            r = run(a,p.at(b));
            if (r > mr) {
                mr = r;
                answer = a*p.at(b);
            }
        }
    }
    return answer;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << " s" << endl;
    return 0;
}
