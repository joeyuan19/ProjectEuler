#include <iostream>
#include <chrono>
#include <cmath>
#include <vector>

using namespace std;

class Finished: public exception {
    virtual const char* what() const throw() {
        return "Finished";
    }
} ex;

int hasRepetition(vector<int> * v) {
    int i, j, l, L;
    //for (l = 2; l < v->size()-1; l++) {
    for (l = v->size()-1; l >= 2; l--) {
        if ((v->size()-1)%l == 0) {
            L = (v->size()-1)/l;
            for (i = 1; i <= L; i++) {
                try {
                    for (j = 1; j < l; j++) {
                        if (v->at(i) != v->at(i+j*L)) {
                            throw ex;
                        }
                    }
                } catch (exception& e) {
                    break;
                }
            }
            if (i == L+1) {
                return L;
            }
        }
    }
    return 0;
}

int solve() {
    int answer = 0;
    int r, n, N = 10000;
    vector<int> v;
    double a, a0, m, d;
    for (n = 2; n <= N; sqrt(n+1) == ((int)sqrt(n+1)) ? n += 2 : n++) {
        a0 = floor(sqrt(n));
        a = a0;
        m = 0;
        d = 1;
        v.push_back(((int)a0));
        r = 0;
        while (v.size() < 100 || r == 0) {
            m = d*a - m;
            d = (n - m*m)/d;
            a = floor((a0+m)/d);
            v.push_back(((int)a));
            r = hasRepetition(&v);
        }
        if (r%2 == 1) {
            answer++;
        }
        v.clear();
    }
    return answer;
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
