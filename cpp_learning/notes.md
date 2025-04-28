# Notes


## Variables
* Place `const` in front of a variable definition to make it immutable:
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
* Use ``const`` instead of using an object-like macro with substitution text 
has different scoping rules. 
* Literals: variables with a meaning that can't be redefined. Can be 
``int``, ``bool``, ``double``, ``char``, ``const char``
    * Floating point literals have type ``double`` by default
    * Use double quotes for string literals, use single quotes for char literals

## Pre-processor
* Removes comments, ensures each code file ends in a new line
* Processes the directives (e.g., ``#include``, ``#define``)

## Macros
* Macro: a rule that defines how input text is converted into replacement output
text. Handled in the pre-processor
* Two types: object-like macros and function-like macros
* Conditional compilation: ``#ifdef``, ``#ifndef``, and ``#endif``
    * ``#ifdef``: allow preprocessor to check whether an identifier has been 
    previously defined via ``#define``. If it is defined, then everything between ``#ifdef`` and ``#endif`` is complied. If not, then the code between 
    those directives is ignored. 
    * ``#ifndef``: allow preprocessor to check whether an identifier has been 
    previously defined via ``#define``. If it has not, then everything between ``#ifndef`` and ``#endif`` is complied. If it is defined, then the code between those directives is ignored. 
    * ``#if0``: exclude everything until ``#endif`` from compiling

### Object-like macros
* 2 ways to define them:
```cpp
#define IDENTIFIER
#define IDENITFIER substitution_text
```
* Seems like another way to define a default value for a variable -- the preprocessor replaces an instance of ``IDENTIFIER`` with ``substitution_text``. 
* If you use a macro with another one (e.g.:
```cpp
#define PRINT_JOE

int main(){
    #ifdef PRINT_JOE
    std::cout << "Joe\n";
    #endif
    return 0;
}
```
) then the macro substitution does not happen. it won't happen when a macro identifier is used within another preprocessor commend -- this way you can use 
macros to check if segments of code are already defined 
* If you include substitution text (which is a constant value), the macro 
becomes a named constant. 

### Function-like macros
* Don't use, just use a function

