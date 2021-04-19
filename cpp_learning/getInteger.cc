#include <iostream>

int getInteger()
{
    std::cout << "Enter an interger: ";
    int x{};
    std::cin >> x;
    return x;
}