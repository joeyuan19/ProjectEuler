#include <iostream>

using namespace std;

int main() {
    int p = 1, i, N = 20;
    while (true) {
        for (i = 1; i <= N; i++) {
            if (p%i != 0) {
                break;
            }
        }
        if (i == N+1) {
            break;
        }
        p += 1;
    }
    cout << p << endl;
    return 0;
}

