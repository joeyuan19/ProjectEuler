#ifndef LARGEN_H
#define LARGEN_H

#include <vector>
#include <string>

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

class Large {
    std::vector<int> number;
    int size;
    public:
        Large() {
            size = 0;
        };
        Large(int _size, int n) {
            size = _size;
            number.resize(size);
            int i = size-1;
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
            for (int i = 0; i < size; i++) {
                if (start) {
                    s += i_to_c(number.at(i));
                } else if (number.at(i) != 0) {
                    start = true;
                    s += i_to_c(number.at(i));
                }
            }
            return s;
        };
        void copy(Large * n) {
            size = n->size;
            number.resize(size);
            for (int i = 0; i < size; i++) {
                number[i] = n->number.at(i);
            }
        }
        void resize(int new_size) {
            if (new_size <= size) {
                return;
            }
            int delta = new_size - size;
            number.resize(new_size);
            for (int i = size-1; i >= 0; i--) {
                number[i-delta] = number[i];
                number[i] = 0;
            }
            size = new_size;
        };
        void multiply(int n) {
            int tmp = 0, s;
            for (int i = size-1; i >= 0; i--) {
                s = number[i]*n+tmp;
                number[i] = s%10;
                tmp = s/10;
            }
        }
        void add(Large n) {
            int tmp = 0, s;
            for (int i = n.size-1; i >= 0; i--) {
                s = number[i]+n.number[i]+tmp;
                number[i] = s%10;
                tmp = s/10;
            }
        };
        int get(int i) {
            if (i >= 0 && i < size) {
                return number.at(i);
            } else {
                return -1;
            }
        }
};


#endif
