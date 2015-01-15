#include <iostream>
#include <ctime>

using namespace std;

int get_month_days(int month, int year) {
    switch (month) {
        case 4:
        case 9:
        case 6:
        case 11:
            return 30;
        case 2:
            if (year%4 == 0) {
                if (year%100 == 0 && year%400 != 0) {
                    return 28;
                } else {
                    return 29;
                }
            } else {
                return 28;
            }
        default:
            return 31;
    }
}


int solve() {
    int year, month, day = 1, a = 0;
    for (year = 1900; year <= 2000; year++) {
        for (month = 1; month <= 12; month++) {
            day = day + get_month_days(month,year);
            if (year > 1900 && day%7 == 0) {
                a += 1;
            }
        }
    }
    return a;
}

int main() {
    time_t start, end;
    time(&start);
    cout << "Answer: " << solve() << endl;
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
