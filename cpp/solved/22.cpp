#include <iostream>
#include <ctime>
#include <cstdio>
#include <fstream>
#include <vector>

using namespace std;

void sort(vector<string> * v) {
    int i;
    string tmp;
    bool swapMade = true;
    while (swapMade) {
        swapMade = false;
        for (i = 0; i < v->size()-1; i++) {
            if (v->at(i).compare(v->at(i+1)) > 0) {
                tmp = v->at(i);
                v->operator[](i) = v->at(i+1);
                v->operator[](i+1) = tmp;
                swapMade = true;
            }
        }
    }
}

int score(string name) {
    int s = 0;
    for (int i = 0; i < name.length(); i++) {
        s += (int)(name[i])-(int)('A')+1;
    }
    return s;
}

long solve() {
    vector<string> names;
    string line;
    ifstream f;
    f.open("files/22.txt");
    char quote = '"', sep = ',', c;
    int i, j = 0;
    string buf = "";
    if (f.is_open()) {
        while (getline(f,line)) {
            buf = "";
            for (i = 0; i < line.length(); i++) {
                c = line[i];
                if (c == quote) {
                    // pass
                } else if (c == sep) {
                    names.push_back(buf);
                    buf = "";
                } else {
                    buf += c;
                }
            }
            if (buf.length() > 0) {
                names.push_back(buf);
            }
        }    
    }
    f.close();
    sort(&names);
    long a = 0;
    for (i = 0; i < names.size(); i++) {
        a += (i+1)*score(names.at(i));
    }
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
