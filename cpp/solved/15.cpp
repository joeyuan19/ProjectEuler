#include <iostream>
#include <ctime>
#include <string>
#include <cmath>

using namespace std;

const int N = 21;
long grid [N*N];

long get(int x, int y) {
    if (x < 0 || x >= N || y < 0 || y >= N) {
        return 0;
    }
    return grid[x*N + y];
}

void set(int x, int y, long n) {
    grid[x*N + y] = n;
}

long solve() {
    set(0,0,1);
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            if (!(j == 0 && i == 0)) {
                set(i,j,get(i-1,j)+get(i,j-1));
            }
        }
    }
    cout << endl;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            cout << get(i,j) << " ";
        }
        cout << endl;
    }
    return get(N-1,N-1);
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
