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