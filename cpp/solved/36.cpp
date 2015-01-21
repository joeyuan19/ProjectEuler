#include <iostream>
#include <chrono>
#include <vector>
#include "helper/largen.h"
#include "helper/print.h"

using namespace std;

vector<int> toBinary(int n) {
    vector<int> v;
    if (n == 0) {
        v.push_back(0);
    } else {
        int tmp = n;
        while (tmp > 0) {
            v.insert(v.begin(),tmp%2);
            tmp = tmp/2;
        }
    }
    return v;
}

bool palindrome(vector<int> n) {
    for (int i = 0; i < n.size()/2; i++) {
        if (n.at(i) != n.at(n.size()-1-i)) {
            return false;
        }
    }
    return true;
}

int solve() {
    int N = 1000000;
    int s = 0;
    for (int i = 0; i < N; i++) {
        if (palindrome(Large(i).getNumber()) && palindrome(toBinary(i))) {
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
