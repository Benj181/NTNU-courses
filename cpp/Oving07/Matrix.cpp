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
Matrix::Matrix(const Matrix & rhs){
    rows = rhs.rows;
    columns = rhs.columns;
    matrix = new double[static_cast<size_t>(rows) * static_cast<size_t>(columns)]();
    for (int i = 0; i < rows*columns; i++){
        matrix[i] = rhs.matrix[i];
    }
}
// END: 4a

// BEGIN: 4b
Matrix& Matrix::operator=(Matrix rhs) {
    std::swap(rows, rhs.rows);
    std::swap(columns, rhs.columns);
    std::swap(matrix, rhs.matrix);
    return *this;
}
// END: 4b


// BEGIN: 5a
Matrix& Matrix::operator+=(const Matrix rhs){
    assert(rows == rhs.rows && columns == rhs.columns);
    for (int i = 0; i < rows*columns; i++){
        matrix[i] += rhs.matrix[i];
    }
    return *this;
}

// END: 5a

// BEGIN: 5b
Matrix Matrix::operator+(const Matrix rhs){
    assert(rows == rhs.rows && columns == rhs.columns);
    Matrix m{rhs};
    for (int i = 0; i < rows*columns; i++){
        m.matrix[i] = matrix[i] + rhs.matrix[i];
    }
    return m;
}
// END: 5b


void testMatrix(){
	Matrix A{2};
	A.set(0, 0, 1.0);
	A.set(0, 1, 2.0);
	A.set(1, 0, 3.0);
	A.set(1, 1, 4.0);
	Matrix B{2};
	B.set(0, 0, 4.0);
	B.set(0, 1, 3.0);
	B.set(1, 0, 2.0);
	B.set(1, 1, 1.0);
	Matrix C{2};
	C.set(0, 0, 1.0);
	C.set(0, 1, 3.0);
	C.set(1, 0, 1.5);
	C.set(1, 1, 2.0);

	A += B + C;
    std::cout << A << std::endl;
    std::cout << B << std::endl;
    std::cout << C << std::endl;
}

// Her kan du gjøre 5d (frivillig):