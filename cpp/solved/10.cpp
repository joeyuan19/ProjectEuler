#include <iostream>
#include <vector>

using namespace std;

vector<int> sieve(int n) {
    vector<int> s (n);
    int i, j, k;
    for (i = 3; i <= n; i += 2) {
        for (j = i; j <= n; j += i) {
            s[j] += 1; 
        }
    }
    vector<int> v;
    v.push_back(2);
    for (i = 3; i < n; i += 2) {
        if (s[i] == 1) {
            v.push_back(i);
        }
    }
    return v;
}

int main() {
    int N = 2000000;
    vector<int> v;
    v = sieve(N);
    
    int i;
    long s = 0;
    cout << v.size() << endl;
    for (i = 0; i < v.size(); i++) {
        cout << v[i] << ",";
        s += v[i];
    }
    cout << endl;
    cout << "Answer: " << s << endl;
    return 0;
}
