#include <iostream>
#include <ctime>


void solve() {
    
    

}

int main() {
    time_t start, end;
    cout << "Answer: " << time(&start) << endl;
    solve();
    time(&end);
    cout << "Time: " << difftime(end,start) << endl;
    return 0;
}
