#include <iostream>

using namespace std;

int main(){
    int x = 0;
    int i = 0;
    for (i = 0; i < 1000; i++) {
        if (i%5 == 0 or i%3 == 0) {
            x + i;
        }
    }
    
    cout << x << endl;
    
    return 0;
} // end main

