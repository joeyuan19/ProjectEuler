#include <iostream>
#include <cmath>

using namespace std;


int factors(int n) {
    int s = 1, i;
    for (i = 1; i*i < n; i++) {
        if (n%i == 0) {
            s += 2;
        }
    }
    if (i*i == n) {
        s += 1;
    }
    return s;
}

int tri(int n) {
    return n*(n+1)/2;
}

int main() {
    int tmp, f, n = 1;
    while (true) {
        if ((f = factors((tmp = tri(n)))) > 500) {
            break;
        }
        n++;
    }
    cout << "Answer: " << n << " with " << tmp << endl;
    
    return 0;
}
