#include <iostream>

int getValue() 
{
    std::cout << "Enter integer: ";
    int input{};
    std::cin >> input;
    
    return input;
}

int main()
{
    int x{getValue()};
    int y{getValue()}; 
    std::cout << "Double " << x << " is: " << x*2 << "\n";
    std::cout << x << " + " << y << " = " << x+y << "\n";

	return 0;
}