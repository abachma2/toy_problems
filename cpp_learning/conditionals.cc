#include <iostream>

bool checkValue(int x)
{
    return(x == 2 || x == 3 || x == 5 || x == 7);
}

int main()
{ 
    std::cout << "Enter a number between 0 and 9: ";
    int x;
    std::cin >> x;

    if (checkValue(x))
        std::cout << "The digit is prime\n";
    else
        std::cout << "The digit is not prime\n";

    return 0;
}