#include <iostream>
#include <chrono>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int score(char c) {
    return ((int)c)-((int)'A')+1;
}

int score(string word) {
    int s = 0;
    for (int i = 0; i < word.length(); i++) {
        s += score(word[i]);
    }
    return s;
}

bool isTri(int n) {
    int i = 1;
    while (2*n > i*i + i) {
        i += 1;
    }
    return 2*n == i*i + i;
}

bool isTriWord(string word) {
    return isTri(score(word));
}

vector<string> parseCSV(string line) {
    char quote = '"';
    char sep = ',';
    string buf = "";
    vector<string> v;
    for (int i = 0; i < line.length(); i++) {
        if (line[i] == quote) {
        } else if (line[i] == sep) {
            v.push_back(buf);
            buf = "";
        } else {
            buf += line[i];
        }
    }
    if (buf.length() > 0) {
        v.push_back(buf);
    }
    return v;
}


int solve() {
    int a = 0;
    vector<string> words;
    string line;
    ifstream f;
    f.open("files/42.txt");
    if (f.is_open()) {
        while (getline(f,line)) {
            words = parseCSV(line);
            for (int i = 0; i < words.size(); i++) {
                if (isTriWord(words.at(i))) {
                    a++;
                }
            }
        }
    }
    return a;
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
