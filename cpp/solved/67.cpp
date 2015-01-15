#include <iostream>
#include <ctime>
#include <fstream>
#include <vector>
#include <string>
#include "helper/stringfix.h"

using namespace std;


vector<int> line_to_row(string line) {
    vector<int> row;
    string buf;
    for (int i = 0; i < line.length(); i++) {
        if (line.at(i) == ' ') {
            row.push_back(stoi(buf));
            buf = "";
        } else {
            buf += line.at(i);
        }
    }
    row.push_back(stoi(buf));
    return row;
}

void p(vector<int> * v) {
    for (int i = 0; i < v->size(); i++) {
        cout << v->at(i) << ", ";
    }
    cout << endl;
}

int solve() {
    vector<int> prev, next;
    bool first = true;
    int i;
    string line;
    ifstream f;
    f.open("files/67.txt");
    if (f.is_open()) {
        while (getline(f,line)) {
            if (first) {
                first = false;
                prev = line_to_row(line);
            } else {
                next = line_to_row(line);
                next.at(0) += prev.at(0);
                next.at(1) += prev.at(0);
                for (i = 1; i < prev.size(); i++) {
                    if (next.at(i) < next.at(i)-prev.at(i-1)+prev.at(i)) {
                        next.at(i) = next.at(i)-prev.at(i-1)+prev.at(i);
                    }
                    next.at(i+1) = next.at(i+1)+prev.at(i);
                }
                prev = next;
            }
        }
    }
    f.close();
    int m = 0;
    for (i = 0; i < next.size(); i++) {
        if (m < next.at(i)) {
            m = next.at(i);
        }
    }
    return m;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
