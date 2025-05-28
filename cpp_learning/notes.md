# Notes


## Variables
1. Place `const` in front of a variable definition to make it immutable:
```cpp
const double gravity {9.8}; // preferred use of a const before type
int const sidesInSquare {4}; // works, but not preferred
```
This can also be applied to function parameters or outputs:
```cpp
void printInt(const int x){
    std::cout << x << '\n';
}

const int getValue(){
    return 5;
}
```
## Macros
* Macro: a rule that defines how input text is converted into replacement output
text
* Two types: object-like macros and function-like macros
### Object-like macros
* 2 ways to define them:
```cpp
#define IDENTIFIER
#define IDENITFIER substitution_text
```
* Seems like another way to define a default value for a variable -- the preprocessor replaces 
an instance of ``IDENTIFIER`` with ``substitution_text``. 

### Function-like macros
* Don't use, just use a function

## Pre-processor
* Removes comments, ensures each code file ends in a new line
* Processes the directives (e.g., ``#include``, ``#define``)

## Function Overloading
* A way to create multiple functions with the same name -- need different parameter 
types
```c++
int add (int x, int y){
    return x+y;
}
double add (double x, double y){
    return x+y;
}
```
* Overloaded functions must be differentiable -- type signatures
    * Different number of input parameters
    * Types of input parameters
    * Not the type aliases (typedefs) or ``const``
    * Not the return type
* Three ways to solve ambiguous overloads:
    * Define a new overloaded method to use the data type you want
    * Explicitly cast arguments to the data type
    * Use a literal suffix