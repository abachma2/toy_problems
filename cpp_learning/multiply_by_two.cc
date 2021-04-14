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
    int number{getValue()}; 
    std::cout << "Double " << number << " is: " << number*2 << "\n";

	return 0;
}