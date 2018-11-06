#include <iostream>
#include <chrono>
#include <string>
#include <map>
#include "helper/stringfix.h"

using namespace std;

class Data {
    int _count;
    long _min;
    public:
        Data () {
            _count = 0;
            _min = 0;
        };
        Data (int c, long m) {
            _count = c;
            _min = m;
        };
        long min() {
            return _min;
        };
        int count() {
            return _count;
        };
        void inc() {
            _count++;
        };
};

string sort(string s) {
    string t = "";
    int i, j;
    for (i = 0; i < s.size(); i++) {
        for (j = 0; j < t.size(); j++) {
            if (s[i] < t[j]) {
                break;
            }
        }
        t = t.substr(0,j) + s[i] + t.substr(j,t.size()-j);
    }
    return t;
}

long solve() {
    map<string,Data> dict;
    string tmp;
    long a;
    for (long i = 1; ; i++) {
        a = i*i*i;
        tmp = sort(tostring(a));
        if (dict.find(tmp) == dict.end()) {
            dict[tmp] = Data(1,a);
        } else {
            dict[tmp].inc();
            if (dict[tmp].count() == 5) {
                break;
            }
        }
    }
    return dict[tmp].min();
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
