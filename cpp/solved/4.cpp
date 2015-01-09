#include <iostream>
#include <string>
#include <sstream>

using namespace std;

namespace patch
{
    template < typename T > string to_string( const T& n )
    {
        ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

int palin(int n) {
    int i;
    string s = patch::to_string(n);
    int L = s.length();
    for (i = 0; i < L/2; i++) {
        if ( s[i] != s[L-1-i] ) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int a, b;
    int m = 0;
    for (a = 100; a <= 999; a++) {
        for (b = a; b <= 999; b++) {
            if (palin(a*b) == 1 && m < a*b) {
                m = a*b;
            }
        }
    }
    cout << "Answer: " << m << endl;
    return 0;
}


