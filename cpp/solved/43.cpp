#include <iostream>
#include <chrono>
#include "helper/stringfix.h"
#include "helper/permute.h"
#include "helper/largen.h"
#include "helper/print.h"

using namespace std;

long subLong(int start, int end, long n) {
    return stol(tostring(n).substr(start,end-start));
}

long toLong(vector<int> * number) {
    long n = 0, tmp = 1;
    for (int i = number->size()-1; i >= 0; i--) {
        n += tmp*number->at(i);
        tmp = 10*tmp;
    }
    return n;
}

bool condition(long n) {
    if (tostring(n).length() == 10) {
        vector<int> primes = {2,3,5,7,11,13,17};
        bool works = true;
        for (int i = 0; i < primes.size(); i++) {
            if (subLong(i+1,i+4,n)%primes.at(i) != 0) {
                works = false;
                break;
            }
        }
        return works;
    } else {
        return false;
    }
}

string solve() {
    Large a (0);
    long tmp;
    vector<int> number = {0,1,2,3,4,5,6,7,8,9};
    while (true) {
        tmp = toLong(&number);
        if (condition(tmp)) {
            a.add(tmp);
        }
        if (!permute(&number)) {
            break;
        }
    }
    return a.toString();
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
