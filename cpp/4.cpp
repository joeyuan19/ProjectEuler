#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int palindrome(int n) {
    string s = to_string(n);
    return strlen(s);
}

int main() {
    cout << palindrome(101) << endl;
}


