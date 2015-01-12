#ifndef TOSTRING_H
#define TOSTRING_H

#include <sstream>
#include <string>

template < typename T > std::string tostring( T n ) {
    std::ostringstream stm;
    stm << n;
    return stm.str();
}

#endif
