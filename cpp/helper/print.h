#ifndef PRINT_H
#define PRINT_H

#include <iostream>
#include <vector>

template <typename T> void printVector(std::vector<T> * v) {
    for (int i = 0; i < v->size(); i++) {
        std::cout << v->at(i) << " ";
    }
    std::cout << std::endl;
} 


#endif
