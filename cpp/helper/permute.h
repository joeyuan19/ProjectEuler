#ifndef PERMUTE_H
#define PERMUTE_H

#include <vector>

void sortFrom(std::vector<int> * v, int startFrom) {
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

bool permute(std::vector<int> * v) {
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

#endif
