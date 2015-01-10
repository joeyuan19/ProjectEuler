#include <iostream>

using namespace std;


int prime(int n) {
    if (n == 2) {
        return 1;
    } else if (n < 2 || n%2 == 0) {
        return 0;
    } else {
        int i = 3;
        while (i*i <= n) {
            if (n%i == 0) {
                return 0;
            }
            i += 2;
        }
        return 1;
    }

}

int main() {
    int i = 2, c = 0, N = 10001;
    while (true) {
        if (prime(i) == 1) {
            c += 1;
            cout << i << "," << c << endl;
        }
        if (c == N) {
            break;
        }
        i += 1;
    }
    return 0;
}
