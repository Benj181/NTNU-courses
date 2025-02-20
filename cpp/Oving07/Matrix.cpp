#include "Matrix.h"

// BEGIN: 2b
Matrix::Matrix(int nRows, int nColumns) : rows(nRows), columns(nColumns) {
    assert(nRows > 0);
    assert(nColumns > 0);

    matrix = new double[static_cast<size_t>(rows) * static_cast<size_t>(columns)]();
}

Matrix::Matrix(int nRows) : Matrix(nRows, nRows){
    for (int i = 0; i < nRows; i++){
        matrix[i * (nRows + 1)] = 1;
    }
}

Matrix::~Matrix(){
    delete[] matrix;
}
// END: 2b

// BEGIN: 2c
double Matrix::get(int row, int col) const{
    assert(row >= 0 && row < rows);
    assert(col >= 0 && col < columns);

    return matrix[row * rows + col];
}

void Matrix::set(int row, int col, double value){
    assert(row >= 0 && row < rows);
    assert(col >= 0 && col < columns);

    matrix[row * rows + col] = value;
}
// END: 2c

const double* Matrix::operator[](int row) const {
    assert(row >= 0 && row < rows);
    return &matrix[row * columns];
}

// BEGIN: 2f
std::ostream& operator<<(std::ostream& os, const Matrix& rhs) {
    for (int i = 0; i < rhs.getRows(); ++i) {
        for (int j = 0; j < rhs.getColumns(); ++j) {
            os << rhs.get(i, j) << ' ';
        }
        os << '\n';
    }
    return os;
}
// END: 2f


// BEGIN: 4a

// END: 4a

// BEGIN: 4b

// END: 4b


// BEGIN: 5a

// END: 5a

// BEGIN: 5b

// END: 5b


void testMatrix() {
    // Her kan du teste løsningen din (oppgave 5c):
}

// Her kan du gjøre 5d (frivillig):