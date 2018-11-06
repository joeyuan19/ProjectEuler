#ifndef GEONUMNS_H
#define GEONUMNS_H

#include <cmath>

int triangle(int i) {
    return i*(i+1)/2;
}

bool isTriangular(int x) {
    if (x < 0) {
        return false;
    }
    double n = (sqrt(8.*x + 1.) - 1.)/2.;
    return ((int)n) == n;
}

int square(int i) {
    return i*i;
}

bool isSquare(int x) {
    if (x < 0) {
        return false;
    }
    double n = sqrt(x);
    return ((int)n) == n;
}

int pentagon(int i) {
    return i*(3*i-1)/2;
}

bool isPentagonal(int x) {
    if (x < 0) {
        return false;
    }
    double n = (sqrt(24.*x + 1.) + 1.)/6.;
    return ((int)n) == n;
}

int hexagon(int i) {
    return i*(2*i-1);
}

bool isHexagonal(int x) {
    if (x < 0) {
        return false;
    }
    double n = (sqrt(8.*x + 1.) + 1.)/4.;
    return ((int)n) == n;
}

int heptagon(int i) {
    return i*(5*i-3)/2;
}

bool isHeptagonal(int x) {
    if (x < 0) {
        return false;
    }
    double n = (sqrt(40.*x + 9.) + 3.)/10.;
    return ((int)n) == n;
}

int octagon(int i) {
    return i*(3*i-2);
}

bool isOctagonal(int x) {
    if (x < 0) {
        return false;
    }
    double n = (sqrt(12.*x + 4.) + 2.)/6.;
    return ((int)n) == n;
}

#endif
