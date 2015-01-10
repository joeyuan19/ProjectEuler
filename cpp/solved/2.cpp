#include <iostream>

using namespace std;

int main(){
    int s = 0;
    int a = 0, b = 1;
    int tmp;
    while (b < 4000000) {
        cout << b << endl;
        if (b%2 ==0) {
            s += b;
        }
        tmp = a;
        a = b;
        b = b + tmp;
    }
    
    cout << s << endl;
    
    return 0;
} // end main

