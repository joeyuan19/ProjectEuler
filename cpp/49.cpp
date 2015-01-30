#include <iostream>
#include <chrono>
#include "helper/prime.h"
#include "helper/stringfix.h"
#include "helper/largen.h"

using namespace std;

class TreeNode {
    TreeNode * leftChild;
    TreeNode * rightChild;
    TreeNode * parent;
    int value;
    public:
        TreeNode () {
            this->parent = NULL;
            this->leftChild = NULL;
            this->rightChild = NULL;
        };
        TreeNode (int _value) {
            this->parent = NULL;
            this->leftChild = NULL;
            this->rightChild = NULL;
            this->value = value;
        };
        TreeNode (TreeNode * _parent, int _value) {
            this->leftChild = NULL;
            this->rightChild = NULL;
            this->value = _value;
            this->parent = _parent;
        };
        void setRightChild(TreeNode * _rightChild) {
            this->rightChild = _rightChild;
        };
        void setLeftChild(TreeNode * _leftChild) {
            this->leftChild = _leftChild;
        };
        void setParent(TreeNode * _parent) {
            this->parent = _parent;
        };
        void insert(int _value) {
            if (value > _value) {
                if (leftChild == NULL) {
                    TreeNode newNode (this,_value);
                    setLeftChild(&newNode);
                    return;
                } else {
                    leftChild->insert(_value);
                }
            } else {
                if (rightChild == NULL) {
                    TreeNode newNode (this,_value);
                    setRightChild(newNode);
                    return;
                } else {
                    rightChild->insert(_value);
                }
            }
        };
        int compare(TreeNode n) {
            if (n == NULL) {
                return 1;
            }if (n.value < value) {
                return 1;
            } else if (n.value > value) {
                return 1;
            } else {
                if (n.leftChild == NULL && n.rightChild == NULL) {
                    return 0;
                } else if ((leftChild != NULL && leftChild.compare(n.leftChild) != 0) || (rightChild != NULL && rightChild.compare(n.rightChild) != 0)) {
                    return 1;
                } else {
                    return 0;
                }
            }
        };
        void print() {
            print (0);
        };
        void print(int level) {
            for (int i = 0; i < level; i++) {
                cout << " ";
            }
            leftChild.print(level+1);
            rightChild.print(level+1);
        };
};

vector<int> toVector(int n) {
    vector<int> v;
    int tmp = n;
    while (tmp > 0) {
        v.insert(v.begin(),tmp%10);
        tmp = tmp/10;
    }
    return v;
}

int isPermute(int a, int b) {
    vector<int> v;
    v = toVector(a);
    TreeNode A (v.at(0));
    for (int i = 1; i < v.size(); i++) {
        A.insert(v.at(i));
    }
    v = toVector(b);
    TreeNode B (v.at(0));
    for (int i = 1; i < v.size(); i++) {
        B.insert(v.at(i));
    }
    return A.compare(B);
}


int solve() {
    int i, j, N = 10000, d;
    for (i = 0; i < N; i++) {
        if (prime(i)) {
            d = 1;
            while (tostring(i+2*d).length() == tostring(i).length()) {
                for (j = 1; j < 3; j++) {
                    if (!prime(i+d*j) || !isPermute(i,i+d*j)) {
                        break;
                    }
                }
                if (j == 3) {
                    break;
                }
                d++;
            }
        }
    }
    return 0;
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
