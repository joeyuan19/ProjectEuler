#include <iostream>
#include <ctime>

using namespace std;

long f(long n) {
    if (n <= 1) {
        return 1;
    } else {
        return n*f(n-1);
    }
}


long solve() {
    return f(40)/(2*f(20));
}

int main() {
    time_t start, end;
    cout << "Answer: " << time(&start) << endl;
    solve();
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
