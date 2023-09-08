# MalViz


### Python/C API
wrapper.cpp makes use of this API to interact with Python3 scripts. 
It can also call Python commands directly within the program via 
Documentation: https://docs.python.org/3/c-api/veryhigh.html

### g++ instructions used for compilation using gcc++
g++ wrapper.cpp -o wrapper -I/usr/include/python3.* -lpython3.*
* replace with your current Python3 version

### Dependencies
install python-dev and $locate Python.h to ensure installation was successful
