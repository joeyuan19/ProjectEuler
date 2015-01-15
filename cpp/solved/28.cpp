#include <iostream>
#include <ctime>

using namespace std;

int solve() {
    int N = 1001;
    int s = 1, n = 1, p = 3, i = 0;
    while (p <= N) {
        for (i = 0; i < 4; i++) {
            n += p-1;
            s += n;
        }
        p += 2;
    }
    
    return s;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << " s" << endl;
    return 0;
}
