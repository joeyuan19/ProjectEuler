#include <iostream>
#include <ctime>
#include <string>
#include <vector>

using namespace std;

void sortFrom(vector<int> * v, int startFrom) {
    int tmp, i;
    bool swapMade = true;
    while (swapMade) {
        swapMade = false;
        for (i = startFrom; i < v->size()-1; i++) {
            if (v->at(i) > v->at(i+1)) {
                tmp = v->at(i);
                v->at(i) = v->at(i+1);
                v->at(i+1) = tmp;
                swapMade = true;
            }
        }
    }
}

bool permute(vector<int> * v) {
    int i, j, tmp;
    int md, mi;
    for (i = v->size()-1; i > 0; i--) {
        if (v->at(i) > v->at(i-1)) {
            tmp = v->at(i-1);
            for (j = v->size()-1; j > 0; j--) {
                if (v->at(j) > v->at(i-1)) {
                    break;
                } 
            }
            v->operator[](i-1) = v->at(j);
            v->operator[](j) = tmp;
            sortFrom(v,i);
            return true;
        }
    }
    return false;
}

void print(vector<int> * v) {
    for (int i = 0; i < v->size(); i++) {
        cout << v->at(i);
    }
    cout << endl;
}

char i_to_c(int i) {
    switch(i) {
        case 0:
            return '0';
        case 1:
            return '1';
        case 2:
            return '2';
        case 3:
            return '3';
        case 4:
            return '4';
        case 5:
            return '5';
        case 6:
            return '6';
        case 7:
            return '7';
        case 8:
            return '8';
        case 9:
            return '9';
    }
}

string v_to_s(vector<int> * v) {
    string s = "";
    for (int i = 0; i < v->size(); i++) {
        s += i_to_c(v->at(i));
    }
    return s;
}

int f(int n) {
    int p = 1;
    while (n > 0) {
        p = p*n;
        n--;
    }
    return p;
}

string solve() {
    vector<int> v = {0,1,2,3,4,5,6,7,8,9};
    int i = 0;
    int t = 0;
    while (true) {
        t++;
        if (t == 1000000) {
            break;
        }
        if (!permute(&v)) {
            break;
        }
    }
    return v_to_s(&v);
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << " s" << endl;
    return 0;
}
