#include "helper/tostring.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int c_to_i(char c) {
    switch (c) {
        case '0':
            return 0;
        case '1':
            return 1;
        case '2':
            return 2;
        case '3':
            return 3;
        case '4':
            return 4;
        case '5':
            return 5;
        case '6':
            return 6;
        case '7':
            return 7;
        case '8':
            return 8;
        case '9':
            return 9;
        default:
            return -1;
    }
}

void pprint(vector<int> * v) {
    bool n_start = false;
    for (int i = 0; i < v->size(); i++) {
        if (v->at(i) != 0) {
            n_start = true;
        }
        if (n_start) {
            cout << v->at(i);
        }
    }
    cout << endl;
}

void _add(vector<int> * n, int index, int value) {
    int idx = index;
    int val = n->at(idx) + value;
    while (val >= 10) {
        n->operator[](idx) = val%10;
        idx--;
        val = n->at(idx) + val/10;
    }
    n->operator[](idx) = val;
}

void add(vector<int> * n, string s) {
    int i, k;
    for (k = 1, i = s.length()-1; i >= 0;  i--, k++) {
        _add(n,n->size()-k,c_to_i(s[i]));
    }
}

int main() {
    int i, j, k, N = 100;
    vector<int> n (N);
    string line;
    ifstream f;
    f.open("files/13.txt");
    if (f.is_open()) {
        while (getline(f,line)) {
            add(&n,line);
        }
    }
    pprint(&n);
    f.close();
    return 0;
}
