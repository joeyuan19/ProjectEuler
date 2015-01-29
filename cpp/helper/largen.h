#ifndef LARGEN_H
#define LARGEN_H

#include <iostream>
#include <vector>
#include <string>

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
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
        default:
            return ' ';
    }
}

class Large {
    std::vector<int> number;
    int sign;
    public:
        Large() {
            number.push_back(0);
            sign = 1;
        };
        Large(int n) {
            number.insert(number.begin(),n%10);
            n = n/10;
            while (n != 0) {
                number.insert(number.begin(),n%10);
                n = n/10;
            }
        };
        Large(long n) {
            number.insert(number.begin(),n%10);
            n = n/10;
            while (n != 0) {
                number.insert(number.begin(),n%10);
                n = n/10;
            }
        };
        Large(int _size, int n) {
            number.resize(_size);
            int i = number.size()-1;
            number[i--] = n%10;
            n = n/10;
            while (n != 0 && i >= 0) {
                number[i--] = n%10;
                n = n/10;
            }
        };
        std::string toString() {
            std::string s = "";
            bool start = false;
            for (int i = 0; i < number.size(); i++) {
                if (start) {
                    s += i_to_c(number.at(i));
                } else if (number.at(i) != 0) {
                    start = true;
                    s += i_to_c(number.at(i));
                }
            }
            if (s.length() > 0) {
                return s;
            } else {
                return "0";
            }
        };
        std::vector<int> getNumber() {
            return number;
        }
        void copy(Large * n) {
            number.resize(n->size());
            for (int i = 0; i < number.size(); i++) {
                number[i] = n->number.at(i);
            }
        };
        int size() {
            return number.size();
        }
        void resize(int new_size) {
            if (new_size <= number.size()) {
                return;
            }
            int delta = new_size - number.size();
            number.resize(new_size);
            for (int i = number.size()-1; i >= 0; i--) {
                number[i-delta] = number[i];
                number[i] = 0;
            }
        };
        void multiply(int n) {
            int tmp = 0, s, i;
            for (i = number.size()-1; i >= 0; i--) {
                s = number[i]*n+tmp;
                number[i] = s%10;
                tmp = s/10;
            }
            while (tmp > 0) {
                number.insert(number.begin(),tmp%10),
                tmp = tmp/10;
            }
        };
        void divide(Large n) {
            /*long tmp = n.toLong();
            set(toLong()/n.toLong());*/
        };
        void add(Large n) {
            int tmp = 0, s, i, j, v;
            for (i = n.size()-1, j = number.size()-1; i >= 0; i--,j--) {
                if (j < 0) {
                    s = n.number[i] + tmp;
                    number.insert(number.begin(),s%10);
                } else {
                    s = number[j] + n.number[i] + tmp;
                    number[j] = s%10;
                }
                tmp = s/10;
            }
            while (tmp > 0) {
                number.insert(number.begin(),tmp%10);
                tmp = tmp/10;
            }
        };
        void add(int n) {
            add(Large(n));
        };
        void add(long n) {
            add(Large(n));
        };
        int get(int i) {
            if (0 <= i && i < number.size()) {
                return number.at(i);
            } else if (i < 0) {
                return 0;
            } else {
                return -1;
            }
        };
        int compare(Large num) {
            int m = max(number.size(),num.size());
            int i = number.size()-m;
            int j = num.size()-m;
            for (i = number.size()-m, j = num.size()-m; i < number.size() && j < num.size(); i++, j++) {
                if (get(i) > num.get(j)) {
                    return 1;
                } else if (get(i) < num.get(j)) {
                    return -1;
                }
            }
            return 0;
        };
        int compare(int n) {
            return compare(Large(n));
        };
        long toLong() {
            long s = 0, tmp = 1;
            for (int i = size()-1; i >= 0; i--) {
                s += tmp*get(i);
                tmp = 10*tmp;
            }
            return s;
        };
        int toInt() {
            int s = 0, tmp = 1;
            for (int i = size()-1; i >= 0; i--) {
                s += tmp*get(i);
                tmp = 10*tmp;
            }
            return s;
        };
};


#endif
