#include "Stopwatch.h"
#include <vector>
#include <iostream>
#include <cmath>

// Utdelt program til oppgave 3

// BEGIN 3b
double sumMatrix(std::vector<double> matrix){ 
    // 1D matrix with [] operator
    double sum = 0;
    for (int i = 0; i < matrix.size(); ++i){;
            sum += matrix[i];            
    }
    return sum;
}

void setDiagonalValue(std::vector<double>& matrix, double newValue){
    // 1D matrix with [] operator
    int dimension = static_cast<int>(sqrt(matrix.size()));
    for (int i = 0; i < dimension; ++i) {
        matrix[i * dimension + i] = newValue;
    }
}

void optimizationTask(){
    Stopwatch stopwatch;
    stopwatch.start();
    const int matrixSize = 10000;

    // lager 1d matrise, chache firendly code
    std::vector<double> matrix(matrixSize * matrixSize, 0.0);

    // Setter alle elementer på diagonalen til 0.41
    setDiagonalValue(matrix, 0.41);
    
    // Summerer alle elementene i matrisen
    double total = sumMatrix(matrix);
    double coolerNumber = total + 2;

    std::cout << "TDT" << coolerNumber << std::endl;
    std::cout << "Time taken: " << stopwatch.stop() << "seconds" << std::endl;
}
// END 3b