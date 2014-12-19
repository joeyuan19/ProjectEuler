#include <iostream>
#include <vector>

using namespace std;

vector<int> sieve(int N) {
    vector<int> s (N,0);
    s[2] = 1;
    int i,j;
    for (i = 3; i < N; i += 2) {
        for (j = i; j < N; j += i) {
            s.at(j) += 1;
        }
    }
    vector<int> p;
    for (i = 0; i < N; i++) {
        if (s.at(i) == 1) {
            p.push_back(i);
        }
    }
    return p;
}

int prime(int n) {
    if (n<2 or n%2 == 0) {
        return 0;
    }
    for (int i = 3; i*i < n; i += 2) {
        if (n%i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    long N = 600851475143, i;
    long max;
    for (i = 3; i*i < N; i += 2) {
        if (N%i == 0 and prime(i) == 1) {
            cout << i << endl;
        }
    }
    
    return 0;
}


