#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

bool is_power_of_2(int n) {
    return (n & (n-1)) == 0;
}

void pprint(vector<int> * c) {
    for (int i = 0; i < c->size(); i++) {
        cout << i << ":" << c->at(i) << ", ";
    }
    cout << endl;
}

int collatz(vector<int> * c, int n) {
    int L = c->size();
    try {
        return c->at(n);
    } catch (const out_of_range& e) {
        int r;
        if (n%2 == 0) {
            r = 1 + collatz(c, n/2);
        } else {
            r = 1 + collatz(c, 3*n + 1);
        }
        c->operator[](n) = r;
        return r;
    }
} 

int main() {
    vector<int> v (2);
    v[0] = 0;
    v[1] = 1;
    int N = 1000;
    int i, mi;
    int c, mc = 0;
    for (i = 2; i < N; i++) {
        c = collatz(&v,i);
        cout << i << " : " << c << endl;
        if (c > mc) {
            mc = c;
            mi = i;
        }
    }
    cout << mi << " : " << mc << endl;
    return 0;
}
