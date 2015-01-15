#ifndef INDEX_H
#define INDEX_H

#include <vector>

class Index {
    public:
        Index(std::vector<int>);
        std::vector<int> indices;
        std::vector<int> limits;
        void reset() {
            for (int i = 0; i < indices.size(); i++) {
                indices[i] = 0;
            }
        };
        bool finished() {
            for (int i = 0; i < indices.size(); i++) {
                if (indices[i] != limits[i]) {
                    return false;
                }
            }
            return true;
        };
        bool next() {
            for (int i = 0; i < indices.size(); i++) {
                if (indices.at(i) == limits.at(i)) {
                    while (i < indices.size() && indices.at(i) == limits.at(i)) {
                        i++;
                    }
                    if (i == indices.size()) {
                        return false;
                    } else {
                        indices[i] += 1;
                        for (int j = 0; j < i; j++) {
                            indices[j] = 0;
                        }
                        return true;
                    }
                } else {
                    indices[i] += 1;
                    return true;
                }
            }
        }
};

Index::Index(std::vector<int> lims) {
    indices.resize(lims.size());
    limits.resize(lims.size());
    for (int i = 0; i < lims.size(); i++) {
        limits[i] = lims[i];
        indices[i] = 0;
    }
}

#endif

