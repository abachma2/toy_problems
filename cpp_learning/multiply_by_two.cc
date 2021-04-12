#include <iostream>
 
int main()
{

    std::cout << "Enter an integer: ";
    int x{0}; 
	std::cin >> x;
    std::cout << "Double that number is: " << x*2 << "\n";
	return 0;
}