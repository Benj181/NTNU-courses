#pragma once
#include <iostream>
#include <utility>
#include <cassert>


class Matrix {
private:
// BEGIN: 2a
    const int rows;
    const int columns;
    double* matrix;
// END: 2a
public:
    // BEGIN: 2b
    Matrix(int nRows, int nColumns);
    explicit Matrix(int nRows);
    ~Matrix();
    // END: 2b
    
    // BEGIN: 2c
    double get(int row, int col) const;
    void set(int row, int col, double value);
    // END: 2c

    // Her kan du gjøre 2d (frivillig):
 

    // BEGIN: 2e
    
    // END: 2e

    
    // BEGIN: 4a
    
    // END: 4a

    // BEGIN: 4b
    
    // END: 4b


    // BEGIN: 5a
    
    // END: 5a

    // BEGIN: 5b
    
    // END: 5b

    // Her kan du gjøre 5d (frivillig):
    
};


// BEGIN: 2f

// END: 2f

void testMatrix();
