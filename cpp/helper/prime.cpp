#include <vector>

bool prime(int n) {
    if (n == 2) {
        return true;
    } else if (n < 2 || n%2 == 0) {
        return false;
    } else {
        for (int i = 3; i*i <= n; i += 2) {
            if (n%i == 0) {
                return false;
            }
        }
        return true;
    }
}

std::vector<int> sieve(int n) {
    std::vector<int> s (n+1,1);
    s[0] = 0;
    s[1] = 0;
    int i, j;
    for (i = 4; i <= n; i += 2) {
        s[i] = 0;
    }
    for (i = 3; i*i <= n; i += 2) {
        if (s[i] == 1) {
            for (j = 2*i; j <= n; j += i) {
                s[j] = 0;
            }
        }
    }
    return s;
}
std::vector<int> primes_up_to(int n) {
    vector<int> s;
    s = sieve(n);
    std::vector<int> p;
    for (i = 0; i <= n; i++) {
        if (s[i] == 1) {
            p.push_back(i);
        }
    }
    return p;

}
