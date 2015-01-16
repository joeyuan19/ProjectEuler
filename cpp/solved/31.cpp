#include <iostream>
#include <chrono>
#include <vector>

using namespace std;

int solve() {
    int N = 200;
    vector<int> v = {1,2,5,10,20,50,100,200};
    vector<int> p (N+1,0);
    p[0] = 1;
    int change, i, coin;
    for (i = 0; i < v.size(); i++) {
        coin = v.at(i);
        for (change = coin; change < p.size(); change++) {
            p[change] += p[change-coin];
        }
    }
    return p[N];
}

int main() {
    typedef chrono::high_resolution_clock Clock;
    typedef chrono::milliseconds milliseconds;
    Clock::time_point start = Clock::now();
    cout << "Answer: " << solve() << endl;
    Clock::time_point end = Clock::now();
    milliseconds ms = chrono::duration_cast<milliseconds>(end-start);
    cout << "Time: " << ms.count() << " ms" << endl;
    return 0;
}
