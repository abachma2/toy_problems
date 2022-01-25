#include <iostream>

int getInteger(); // forward declaring the function

int main()
{
    int x{getInteger()};
    int y{getInteger()};

    std::cout << x << " * " << y << " is " << x*y << "\n";
    return 0;
}