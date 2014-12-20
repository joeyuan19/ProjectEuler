#include <iostream>
#include <cstring>
#include <string>

int palindrome(int n) {
    std::string s = std::to_string(n);
    return strlen(s);
}

int main() {
    std::cout << palindrome(101) << std::endl;
}


