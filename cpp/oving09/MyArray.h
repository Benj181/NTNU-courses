#pragma once
#include <iostream>
#include <exception>

// BEGIN 5a
template<typename Type, int Size>
// END 5a
class MyArray
{
    private:
        // BEGIN 5b
        Type elements[Size];
        // END 5b
    public:
        // BEGIN 5c
        int getSize(){
            return Size;
        }

        Type& at(int i) {
            if (i < 0 || i >= Size) {
                throw std::out_of_range("Indeks utenfor gyldig område");
            }
            return elements[i];
        }
    
        void fill(Type val) {
            for (int i = 0; i < Size; ++i) {
                elements[i] = val;
            }
        }
        // END 5c
};

// BEGIN 5d
void testMyArray();
// END 5d