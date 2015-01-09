#include <iostream>

using namespace std;

int main() {
    int s1, s2, i, N = 100;
    for (i = 1; i <= N; i++) {
        s1 += i;
        s2 += i*i;
    }
    cout << s1*s1 - s2 << endl;
    return 0;
}
