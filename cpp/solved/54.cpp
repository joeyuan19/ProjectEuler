#include <iostream>
#include <chrono>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include "helper/stringfix.h"

using namespace std;

const int TWO   = 2;
const int THREE = 3;
const int FOUR  = 4;
const int FIVE  = 5;
const int SIX   = 6;
const int SEVEN = 7;
const int EIGHT = 8;
const int NINE  = 9;
const int TEN   = 10;
const int JACK  = 11;
const int QUEEN = 12;
const int KING  = 13;
const int ACE   = 14;

const int SPADES   = 1;
const int HEARTS   = 2;
const int DIAMONDS = 3;
const int CLUBS    = 4;

int suitValue(char c) {
    switch (c) {
        case 'S':
            return SPADES;
        case 'H':
            return HEARTS;
        case 'D':
            return DIAMONDS;
        case 'C':
            return CLUBS;
        default:
            return 0;
    }
}

int cardValue(char c) {
    switch (c) {
        case '2':
            return TWO;
        case '3':
            return THREE;
        case '4':
            return FOUR;
        case '5':
            return FIVE;
        case '6':
            return SIX;
        case '7':
            return SEVEN;
        case '8':
            return EIGHT;
        case '9':
            return NINE;
        case 'T':
            return TEN;
        case 'J':
            return JACK;
        case 'Q':
            return QUEEN;
        case 'K':
            return KING;
        case 'A':
            return ACE;
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

int highCard(vector<Card> * cards) {
    int m = 0, i;
    for (i = 0; i < cards->size(); i++) {
        if (cards->at(i).value() > m) {
            m = cards->at(i).value();
        }
    }
    return m;
}

int onePair(vector<Card> * cards) {
    int i;
    vector<int> hist;
    for (i = 0; i <= ACE; i++) {
        hist.push_back(0);
    }
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    for (i = ACE; i >= TWO; i--) {
        if (hist[i] == 2) {
            return i+1000;
        }
    }
    return 0;
}

int twoPair(vector<Card> * cards) {
    int i;
    vector<int> hist;
    for (i = 0; i <= ACE; i++) {
        hist.push_back(0);
    }
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    int c = 0;
    int p1 = -1, p2 = -1;
    for (i = ACE; i >= TWO; i--) {
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
        return 2000 + (p2-2)*13 + p1 + p2;
    } else {
        return 0;
    }
}

int threeOfAKind(vector<Card> * cards) {
    int i;
    vector<int> hist;
    for (i = 0; i <= ACE; i++) {
        hist.push_back(0);
    }
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    for (i = ACE; i >= TWO; i--) {
        if (hist[i] == 3) {
            return i+3000;
        }
    }
    return 0;
}

int straight(vector<Card> * cards) {
    sort(cards);
    if (cards->at(0).value() == TWO && cards->at(4).value() == ACE) {
        for (int i = 1; i < cards->size()-1; i++) {
            if (cards->at(i).value() != cards->at(i-1).value() + 1) {
                return 0;
            }
        }
        return 4000;
    } else {
        for (int i = 1; i < cards->size(); i++) {
            if (cards->at(i).value() != cards->at(i-1).value() + 1) {
                return 0;
            }
        }
        return 4001 + cards->at(0).value();
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
            return 5000;
        }
    }
    return 0;
}

int fullHouse(vector<Card> * cards) {
    int i;
    vector<int> hist = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}; 
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    int p1 = -1, p2 = -1;
    for (i = ACE; i >= TWO; i--) {
        if (hist[i] == 2) {
            p1 = i;
        }
        if (hist[i] == 3) {
            p2 = i;
        }
    }
    if (p1 > 0 && p2 > 0) {
        return 6000 + (p1-2)*13 + p1 + p2;
    } else {
        return 0;
    }
}

int fourOfAKind(vector<Card> * cards) {
    int i;
    vector<int> hist = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}; 
    for (i = 0; i < cards->size(); i++) {
        hist[cards->at(i).value()]++;
    }
    for (i = ACE; i >= TWO; i--) {
        if (hist[i] == 4) {
            return i+7000;
        }
    }
    return 0;
}

int straightFlush(vector<Card> * cards) {
    sort(cards);
    if (straight(cards) > 0 && flush(cards) > 0) {
        return 8000 + cards->at(0).value();
    } else {
        return 0;
    }
}

int royalFlush(vector<Card> * cards) {
    sort(cards);
    if (cards->at(0).value() == TEN && straight(cards) > 0 && flush(cards) > 0) {
        return 9000;
    } else {
        return 0;
    }
}

int valueHand(vector<Card> * cards) {
    int score;
    if ((score = royalFlush(cards)) > 0) {
        //cout << "royalFlush" << endl;
        return score;
    } else if ((score = straightFlush(cards)) > 0) {
        //cout << "straightFlush" << endl;
        return score;
    } else if ((score = fourOfAKind(cards)) > 0) {
        //cout << "fourOfAKind" << endl;
        return score;
    } else if ((score = fullHouse(cards)) > 0) {
        //cout << "fullHouse" << endl;
        return score;
    } else if ((score = flush(cards)) > 0) {
        //cout << "flush" << endl;
        return score;
    } else if ((score = straight(cards)) > 0) {
        //cout << "straight" << endl;
        return score;
    } else if ((score = threeOfAKind(cards)) > 0) {
        //cout << "threeOfAKind" << endl;
        return score;
    } else if ((score = twoPair(cards)) > 0) {
        //cout << "twoPair" << endl;
        return score;
    } else if ((score = onePair(cards)) > 0) {
        //cout << "onePair" << endl;
        return score;
    } else {
        //cout << "highCard" << endl;
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
        vector<Card> * getCards() {
            return &cards;
        };
        Card get(int i) {
            return cards.at(i);
        };
        void sortCards() {
            sort(&cards);
        };
};

int tieBreaker(Hand h1, Hand h2) {
    h1.sortCards();
    h2.sortCards();
    for (int i = 4; i >= 0; i--) {
        if (h1.get(i).value() > h2.get(i).value()) {
            return 1;
        } else if (h1.get(i).value() < h2.get(i).value()) {
            return 0;
        }
    }
    return 0;
}


int determineWinner(string s) {
    string p1 = s.substr(0,s.size()/2), p2 = s.substr(s.size()/2+1,s.size()/2);
    Hand h1 (p1), h2 (p2);
    int r1 = h1.handRank(), r2 = h2.handRank();
    if (r1 > r2) {
        //cout << s << " winner: " << (1) << endl;
        //cout << "r1 = " << r1 << " r2 = " << r2 << endl;
        return 1;
    } else if (r1 == r2) {
        //cout << "####################### TIE ###########################" << endl;
        return tieBreaker(h1,h2);
    } else {
        return 0;
    }
}

int solve() {
    int a = 0, r;
    string line;
    ifstream f;
    f.open("files/54.txt");
    if (f.is_open()) {
        while (getline(f,line)) {
            r = determineWinner(line);
            a += r;
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
