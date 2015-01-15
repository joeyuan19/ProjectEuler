#include <iostream>
#include <ctime>
#include <vector>

using namespace std;

void m(vector<int> * v, int n) {
    int tmp = 0, i;
    for (i = v->size()-1; i >= 0; i--) {
        tmp = v->at(i)*n + tmp;
        v->operator[](i) = tmp%10;
        tmp = tmp/10;
    }
}

void p(vector<int> * v) {
    bool print = false;
    for (int i = 0; i < v->size(); i++) {
        if (!print && v->at(i) != 0) {
            print = true;
        }
        if (print) {
            cout << v->at(i);
        }
    }
    cout << endl;
}

int solve() {
    int L = 1000, N = 100, i;
    vector<int> v (L,0);
    v[L-1] = 1;
    for (i = 2; i <= N; i++) {
        m(&v,i);
    }
    int a = 0;
    for (i = 0; i < v.size(); i++) {
        a += v.at(i);
    }
    p(&v);
    return a;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
