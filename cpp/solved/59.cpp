#include <iostream>
#include <chrono>
#include <vector>
#include <cctype>
#include <string>
#include <fstream>
#include "helper/stringfix.h"

using namespace std;

class WordDictionary {
    vector<string> words;
    public:
        WordDictionary (string filepath) {
            ifstream f;
            string line;
            f.open(filepath);
            if (f.is_open()) {
                while (getline(f,line)) {
                    words.push_back(line);
                }
            }
            f.close();
            sort();
        };
        bool hasWord(string word) {
            
        };
        void sort() {
            int i;
            string tmp;
            bool swap = true;
            while (swap) {
                swap = false;
                for (i = 0; i < words.size()-1; i++) {
                    if (words.at(i).compare(words.at(i+1)) < 0) {
                        tmp = words.at(i);
                        words[i] = words.at(i+1);
                        words[i+1] = tmp;
                        swap = true;
                    }
                }
            }
        };
        int find(string s) {
            for (int i = 0; i < words.size(); i++) {
                if (words.at(i).compare(s) == 0) {
                    return i;
                }
            }
            return -1;
        };

};

vector<string> getWords(string s) {
    string buf = "";
    int i;
    vector<string> words;
    for (i = 0; i < s.size(); i++) {
        if (isspace(s.at(i))) {
            if (buf.size() > 0) {
                words.push_back(buf);
                buf = "";
            }
        } else {
            buf += s.at(i);
        }
    }
    if (buf.size() > 0) {
        words.push_back(buf);
    }
    return words;
}

vector<int> _decode(vector<int> c, string password) {
    vector<int> _c;
    for (int i = 0; i < c.size(); i++) {
        _c.push_back(c.at(i)^((int)password[i%password.size()]));
    }
    return _c;
}

string toString(vector<int> c) {
    string s = "";
    for (int i = 0; i < c.size(); i++) {
        s += ((char)c.at(i));
    }
    return s;
}

string decode(vector<int> c, string password) {
    return toString(_decode(c,password));
}

int solve() {
    WordDictionary wd ("files/59_words.txt");
    vector<int> cipher;
    ifstream f;
    f.open("files/59.txt");
    string line, buf = "";
    int i;
    if (f.is_open()) {
        while (getline(f,line)) {
            buf = "";
            for (i = 0; i < line.size(); i++) {
                if (line.at(i) == ',' && buf.size() > 0) {
                    cipher.push_back(stoi(buf));
                    buf = "";
                } else {
                    buf += line.at(i);
                }
            }
            if (buf.size() > 0) {
                cipher.push_back(stoi(buf));
            }
        }
    }
    f.close();
    
    vector<string> words;
    int realWords = 0;
    double m = 0.0;
    string best = "", pass, tmp;
    char a,b,c;
    for (a = 'a'; a <= 'z'; a++) {
        for (b = 'a'; b <= 'z'; b++) {
            for (c = 'a'; c <= 'z'; c++) {
                pass = "";
                pass += a;
                pass += b;
                pass += c;
                tmp = decode(cipher,pass);
                words = getWords(tmp);
                realWords = 0;
                for (int i = 0; i < words.size(); i++) {
                    if (wd.find(words.at(i)) >= 0) {
                        realWords++;
                    }
                }
                if (((double)realWords)/words.size() > m) {
                    m = ((double)realWords)/words.size();
                    best = pass;
                }
            }
        }
    }
    cout << "Best: " << best << endl;
    tmp = decode(cipher,best);
    cout << "Decoded: " << tmp << endl;

    int s = 0;
    for (i = 0; i < tmp.size(); i++) {
        s += (int) tmp[i];
    }

    return s;
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
