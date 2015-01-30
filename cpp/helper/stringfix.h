#ifndef TOSTRING_H
#define TOSTRING_H

#include <sstream>
#include <string>

template < typename T > std::string tostring( T n ) {
    std::ostringstream stm;
    stm << n;
    return stm.str();
}
int ctoi(char c) {
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
            return 0;
    }
}
char itoc(int c) {
    switch (c) {
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
            return '#';
    }
}
long ctol(char c) {
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
            return 0;
    }
}
int stoi(std::string s) {
    int sum = 0, tmp = 1, i, j;
    for (i = s.length()-1; i >= 0; i--) {
        tmp = 1;
        for (j = i; j < s.length()-1; j++) {
            tmp = tmp*10;
        }
        sum += tmp*ctoi(s.at(i));
    }
    return sum;
}
long stol(std::string s) {
    long sum = 0, tmp = 1, i, j;
    for (i = s.length()-1; i >= 0; i--) {
        tmp = 1;
        for (j = i; j < s.length()-1; j++) {
            tmp = tmp*10;
        }
        sum += tmp*ctol(s.at(i));
    }
    return sum;
}


#endif
