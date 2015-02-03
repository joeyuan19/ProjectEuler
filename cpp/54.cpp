#include <iostream>
#include <chrono>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include "helper/stringfix.h"

using namespace std;

int suitValue(char c) {
    switch (c) {
        case 'S':
            return 1;
        case 'H':
            return 2;
        case 'D':
            return 3;
        case 'C':
            return 4;
        default:
            return 0;
    }
}

int cardValue(char c) {
    switch (c) {
        case '2':
            return 1;
        case '3':
            return 2;
        case '4':
            return 3;
        case '5':
            return 4;
        case '6':
            return 5;
        case '7':
            return 6;
        case '8':
            return 7;
        case '9':
            return 8;
        case 'T':
            return 9;
        case 'J':
            return 10;
        case 'Q':
            return 11;
        case 'K':
            return 12;
        case 'A':
            return 13;
        default:
            return 0;
    }
}

class Card {
    int _suit;
    int _value;
    public:
        Card () {
            _suit = 0;
            _value = 0;
        };
        Card (string s) {
            _suit = suitValue(s[1]);
            _value = cardValue(s[0]);
        };
        int value() {
            return _value;
        };
        int suit() {
            return _suit;
        };
        void copy(Card c) {
            _value = c.value();
            _suit = c.suit();
        }
};

void sort(vector<Card> * cards) {
    int i;
    Card tmp;
    bool swapMade = true;
    while (swapMade) {
        swapMade = false;
        for (i = 0; i < cards->size()-1; i++) {
            if (cards->at(i).value() > cards->at(i+1).value()) {
                tmp.copy(cards->at(i));
                cards->at(i).copy(cards->at(i+1));
                cards->at(i+1).copy(tmp);
                swapMade = true;
            }
        }
    }
}

int highCard(vector<Card> * cards, int limit) {
    int m = 0, i;
    for (i = 0; i < cards->size(); i++) {
        if (cards->at(i).value() > m && cards->at(i).value() < limit) {
            m = cards->at(i).value();
        }
    }
    return m;
}

int highCard(vector<Card> * cards) {
    return highCard(cards,14);
}

int onePair(vector<Card> * cards) {
    int i;
    vector<int> hist = {0,0,0,0,0,0,0,0,0,0,0,0,0,0}; 
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    for (i = 13; i >= 2; i--) {
        if (hist[i] == 2) {
            return i+14;
        }
    }
    return 0;
}

int twoPair(vector<Card> * cards) {
    int i;
    vector<int> hist = {0,0,0,0,0,0,0,0,0,0,0,0,0,0}; 
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    int c = 0;
    int p1 = -1, p2 = -1;
    for (i = 13; i >= 2; i--) {
        if (hist[i] == 2) {
            c++;
            if (p1 < 0) {
                p1 = i;
            } else {
                p2 = i;
            }
        }
    }
    if (c == 2) {
        return 28 + (min(p1,p2)-2)*13 + p1 + p2;
    } else {
        return 0;
    }
}

int threeOfAKind(vector<Card> * cards) {
    int i;
    vector<int> hist = {0,0,0,0,0,0,0,0,0,0,0,0,0,0}; 
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    for (i = 13; i >= 2; i--) {
        if (hist[i] == 3) {
            return i+185;
        }
    }
    return 0;
}

int straight(vector<Card> * cards) {
    sort(cards);
    if (cards->at(0).value() == 2) {
        if (cards->at(4).value() == 13) {
            return 0;
        }
        for (int i = 1; i < cards->size()-1; i++) {
            if (cards->at(i).value() != cards->at(i-1).value() + 1) {
                return 0;
            }
        }
        return 201;
    } else {
        for (int i = 1; i < cards->size(); i++) {
            if (cards->at(i).value() != cards->at(i-1).value() + 1) {
                return 0;
            }
        }
        return 200 + cards->at(0).value();
    }
}

int flush(vector<Card> * cards) {
    vector<int> suits = {0,0,0,0,0};
    int i;
    for (i = 0; i < cards->size(); i++) {
        suits[cards->at(i).suit()]++;
    }
    for (i = 1; i < suits.size(); i++) {
        if (suits[i] == 5) {
            return 220;
        }
    }
    return 0;
}

int fullHouse(vector<Card> * cards) {
    int i;
    vector<int> hist = {0,0,0,0,0,0,0,0,0,0,0,0,0,0}; 
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    int p1 = -1, p2 = -1;
    for (i = 13; i >= 2; i--) {
        if (hist[i] == 2) {
            p1 = i;
        }
        if (hist[i] == 3) {
            p2 = i;
        }
    }
    if (p1 > 0 && p2 > 0) {
        return 221 + (min(p1,p2)-2)*13 + p1 + p2;
    } else {
        return 0;
    }
}

int fourOfAKind(vector<Card> * cards) {
    int i;
    vector<int> hist = {0,0,0,0,0,0,0,0,0,0,0,0,0,0}; 
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    for (i = 13; i >= 2; i--) {
        if (hist[i] == 4) {
            return i+380;
        }
    }
    return 0;
}

int straightFlush(vector<Card> * cards) {
    sort(cards);
    if (straight(cards) > 0 && flush(cards) > 0) {
        return 400 + cards->at(0).value();
    } else {
        return 0;
    }
}

int royalFlush(vector<Card> * cards) {
    sort(cards);
    if (cards->at(0).value() == 10 && straight(cards) > 0 && flush(cards) > 0) {
        return 500;
    } else {
        return 0;
    }
}

int valueHand(vector<Card> * cards) {
    int score;
    if ((score = royalFlush(cards)) > 0) {
        return score;
    } else if ((score = straightFlush(cards)) > 0) {
        return score;
    } else if ((score = fourOfAKind(cards)) > 0) {
        return score;
    } else if ((score = fullHouse(cards)) > 0) {
        return score;
    } else if ((score = flush(cards)) > 0) {
        return score;
    } else if ((score = straight(cards)) > 0) {
        return score;
    } else if ((score = threeOfAKind(cards)) > 0) {
        return score;
    } else if ((score = twoPair(cards)) > 0) {
        return score;
    } else if ((score = onePair(cards)) > 0) {
        return score;
    } else {
        return highCard(cards);
    }
}

class Hand {
    vector<Card> cards;
    public:
        Hand (string hand) {
            string buf = "";
            int i;
            for (i = 0; i < hand.size(); i++) {
                if (hand[i] == ' ') {
                    cards.push_back(Card (buf));
                    buf = "";
                } else {
                    buf += hand[i];
                }
            }
            if (buf.size() > 0) {
                cards.push_back(Card (buf));
            }
        };
        int handRank() {
            return valueHand(&cards);
        };
};


int determineWinner(string s) {
    string p1 = s.substr(0,s.size()/2), p2 = s.substr(s.size()/2+1,s.size()/2);
    Hand h1 (p1), h2 (p2);
    if (h1.handRank() > h2.handRank()) {
        return 1;
    } else {
        return 0;
    }
}

int solve() {
    int a = 0;
    string line;
    ifstream f;
    f.open("files/54.txt");
    if (f.is_open()) {
        while (getline(f,line)) {
            a += determineWinner(line);
        }
    }
    f.close();
    return a;
}

int main() {
    typedef chrono::high_resolution_clock Clock;
    typedef chrono::milliseconds milliseconds;
    Clock::time_point start = Clock::now();
    cout << "Answer: " << solve() << endl;
    Clock::time_point end = Clock::now();
    milliseconds ms = chrono::duration_cast<milliseconds>(end-start);
    cout << "Time: " << ms.count() << " ms" << endl;
    return 0;
}
