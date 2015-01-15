#include <iostream>
#include <ctime>

using namespace std;

string convert(int n) {
    switch (n) {
        case 0:
            return "";
        case 1:
            return "one";
        case 2:
            return "two";
        case 3:
            return "three";
        case 4:
            return "four";
        case 5:
            return "five";
        case 6:
            return "six";
        case 7:
            return "seven";
        case 8:
            return "eight";
        case 9:
            return "nine";
        case 10:
            return "ten";
        case 11:
            return "eleven";
        case 12:
            return "twelve";
        case 13:
            return "thirteen";
        case 14:
            return "fourteen";
        case 15:
            return "fifteen";
        case 16:
            return "sixteen";
        case 17:
            return "seventeen";
        case 18:
            return "eighteen";
        case 19:
            return "nineteen";
        case 20:
            return "twenty";
        case 30:
            return "thirty";
        case 40:
            return "forty";
        case 50:
            return "fifty";
        case 60:
            return "sixty";
        case 70:
            return "seventy";
        case 80:
            return "eighty";
        case 90:
            return "ninety";
        case 100:
            return "onehundred";
        case 200:
            return "twohundred";
        case 300:
            return "threehundred";
        case 400:
            return "fourhundred";
        case 500:
            return "fivehundred";
        case 600:
            return "sixhundred";
        case 700:
            return "sevenhundred";
        case 800:
            return "eighthundred";
        case 900:
            return "ninehundred";
        case 1000:
            return "onethousand";
        defualt:
            cout << "Default: " << n << endl;
            return "";
    }
}

string n_to_s(int n) {
    string s = "";
    if (n == 1000) {
        return convert(n);
    } else if (n >= 100) {
        s += convert(100*(n/100));
        if (n%100 != 0) {
            s += "and";
        }
        if (n%100 >= 20) {
            s += convert(10*((n%100)/10));
            if (n%10 != 0) {
                s += convert(n%10);
            }
        } else {
            s += convert(n%100);
        }
    } else if (n >= 20) {
        s += convert(10*((n%100)/10));
        if (n%10 != 0) {
            s += convert(n%10);
        }
    } else {
        s += convert(n);
    }
    return s;
}

long solve() {
    int i, N = 1000, s = 0;
    for (i = 1; i <= N; i++) {
        s += n_to_s(i).length();
        cout << "s = " << s << " i = " << i << " n_to_s(i) = " << n_to_s(i) << " length = " << n_to_s(i).length() << endl;
    }
    return s;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
