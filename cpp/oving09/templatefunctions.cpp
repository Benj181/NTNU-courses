#include "templatefunctions.h"

void testTemplateFunctions(){
    // Her kan du teste templatefunksjonene dine
    int a = 1;
    int b = 2;
    int c = maximum<int>(a, b);
    std::cout << c << std::endl;

    double d = 2.4;
    double e = 3.2;
    double f = maximum<double>(d,e);
    std::cout << f << std::endl;

    std::vector<int> g{1, 2, 3, 4, 5, 6, 7};
    shuffle(g); 
    std::cout << g << std::endl;
    
    std::vector<double> h{1.2, 2.2, 3.2, 4.2};
    shuffle(h); 
    std::cout << h << std::endl;
    
    std::vector<std::string> i{"one", "two", "three", "four"};
    shuffle(i); 
    std::cout << i << std::endl;

    std::cout << "Done" << std::endl;
}

