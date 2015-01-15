#include <iostream>
#include <ctime>
#include <vector>

using namespace std;

int find(vector<int> * v, int n) {
    for (int i = 0; i < v->size(); i++) {
        if (v->at(i) == n) {
            return i;
        }
    }
    return -1;
}

int divide(int n, int d) {
    vector<int> history;
    int r = 0;
    while (n != 0 && find(&history,n) < 0) {
        history.push_back(n);
        n = (n*10)%d;
        r++;
    }
    if (n == 0) {
        return 0;
    } else {
        return r;
    }
}

int solve() {
    int a = 0, n, N = 1000, md;
    for (int d = 2; d < N; d++) {
        n = divide(1,d);
        if (a < n) {
            a = n;
            md = d;
        }
    }
    return md;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << " s" << endl;
    return 0;
}
