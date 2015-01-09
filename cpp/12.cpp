#include <iostream>
#include <cmath>

using namespace std;


int factors(int n) {
    int s = 1;
    for (int i = 1; i < n/2 + 1; i++) {
        if (n%i == 0) {
            s += 1;
        }
    }
    return s;
}

int tri(int n) {
    int s = 0;
    for (int i = 0; i < n+1; i++) {
        s += i;
    }
    return s;
}

int main() {
    int tmp, f, n = 1;
    while (true) {
        if ((f = factors((tmp = tri(n)))) > 500) {
            break;
        }
        cout << f << endl;
        n++;
    }
    cout << "Answer: " << n << " with " << tmp << endl;
    
    return 0;
}
