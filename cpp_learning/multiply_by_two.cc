#include <iostream>

int getValue() 
{
    std::cout << "Enter integer: ";
    int input{};
    std::cin >> input;
    
    return input;
}

void printDouble(int value)
{
    std::cout << value << " doubled is: " << value*2 << "\n";
}

int main()
{
    int x{getValue()};
    int y{getValue()}; 
    printDouble(x);
    printDouble(y);

	return 0;
}